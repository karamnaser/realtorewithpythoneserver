class SearchBuilder:
    def __init__(self,page=1,size=10):
        self.query={}
        self.page=page;
        self.size=size

    def id(self,id=""):
        if not id:
            return self
        self.query["id"]=id
        return self

    def city(self,city=""):
        if not city:
            return self
        self.query["city"]=city
        return self


    def country(self,country=""):
        if not country:
            return self
        self.query["country"]=country
        return self

    def avilabilty(self,avilabilty=""):
        if not avilabilty:
            return self
        self.query["availability"]=avilabilty
        return self

    def status(self,status=""):
        if not status:
            return self
        self.query["status"]=status
        return self

    def salestate(self,salestate=""):
        if not salestate:
            return self
        self.query["sale_status"]=salestate
        return self

    def roomnumber(self,roomnumber=""):
        if not roomnumber:
            return self
        self.query["numberofrooms"]=roomnumber
        return self

    def bathnumber(self,numberofbaths=""):
        if not numberofbaths:
            return self
        self.query["numberofbaths"]=numberofbaths
        return self

    def price(self,price=""):
        if not price:
            return self
        self.query["price"]=price
        return self


    def build(self):
        return self.query



