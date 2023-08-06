from time import time
from gandai.datastore import Cloudstore
from gandai.models import Event
from gandai.services import Query

ds = Cloudstore()


def load_search(key: str, actor_key: str = "") -> dict:

    def _get_comments(domain: str) -> list:
        if len(comments) == 0:
            return []
        return comments.query("domain == @domain").to_dict(orient="records")

    def _get_events(domain: str) -> list:
        if len(events) == 0:
            return []
        df = events[events['domain'] == domain]
        df = df[df['type'] != 'rating'] # rm fit events
        return df.to_dict(orient="records")
        
    def _get_rating(domain: str) -> int:
        if len(events) == 0:
            return None
        df = events[events['domain'] == domain]
        df = df[df['type'] == 'rating']
        if len(df) == 0:
            return None
        data = df.to_dict(orient="records")[-1]  
        return data['data']['rating']


    def _targets_by_state(last_event_type: str, filters={}) -> list:
        """Apply filters on a per state basis"""
        df = targets.query("last_event_type == @last_event_type")
        if len(df) == 0:
            return []
        for k, v in filters.items():
            if k == 'employee_count':
                df = df[df[k] >= v['min']]
                df = df[df[k] <= v['max']]
            elif k == 'ownership': 
                df = df[df[k].isin(v['include'])]
                df = df[~df[k].isin(v['exclude'])]    
            elif k == 'country': 
                if len(v) > 0:
                    df = df[df['country'].isin(v)]
            elif k == 'state': 
                if len(v) > 0:
                    df = df[df['state'].isin(v)]
            print(k, df.shape)

        if "limit" in filters.keys():
            df = df[0:filters['limit']['results']]

        
        return df.fillna("").to_dict(orient="records")

    t0 = time()
    search_data = ds[f"searches/{key}/search"]
    companies = Query.companies_query(key)
    events = Query.events_query(key)
    comments = Query.comments_query(key)
    conflicts = Query.dealcloud_company_query() # conflicts might not be the right word for this
    
    
    companies["comments"] = companies["domain"].apply(_get_comments)
    companies["events"] = companies["domain"].apply(_get_events)
    companies["rating"] = companies["domain"].apply(_get_rating)
    companies["last_event_type"] = companies["events"].apply(
        lambda x: x[-1]["type"] if len(x) > 0 else "created"
    )

    companies = companies.merge(conflicts, how='left', left_on='domain', right_on='domain')
    companies['dealcloud_id'] = companies['dealcloud_id'].fillna("")
    
    targets = companies
    sort = search_data['sort']
    # import pdb ; pdb.set_trace()
    if len(targets) > 0:
        # KeyError: 'employee_count'
        targets = targets.sort_values(list(sort.keys()), ascending=list(sort.values())[0] == 'asc')
    
    print("queries:", (time()-t0))    
    search_data = ds[f"searches/{key}/search"]
    resp = {
        "key": key,
        "actor_key": actor_key,
        "meta": search_data['meta'],
        "keywords": search_data['keywords'],
        "filters": search_data['filters'],
        "do_not_contact": search_data['do_not_contact'],
        "sort": search_data['sort'],
        "companies": {
            "inbox": _targets_by_state("created", filters=search_data['filters']),
            "review": _targets_by_state("advance", filters=search_data['filters']),
            "validate": _targets_by_state("validate"),
            "send": _targets_by_state("send"),
            "accept": _targets_by_state("accept"),
            "reject": _targets_by_state("reject"),
            "conflict": _targets_by_state("conflict")
        },
    }
    return resp
