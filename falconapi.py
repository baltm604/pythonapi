import falcon, json
from waitress import serve

class CompaniesResource(object):
  companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]
  def on_get(self, req, resp):
    resp.body = json.dumps(self.companies)
  
  def on_post(self, req, resp):
    resp.status = falcon.HTTP_201
    resp.body = json.dumps({"success": True})    

class PeopleResource(object):
  people = [{"id": 1, "name": "Bill"}, {"id": 2, "name": "Jane"}]
  def on_get(self, req, resp):
    resp.body = json.dumps(self.people)

api = falcon.API()
companies_endpoint = CompaniesResource()
people_endpoint = PeopleResource()
api.add_route('/companies', companies_endpoint)
api.add_route('/people', people_endpoint)
serve(api, host='0.0.0.0', port=8000)