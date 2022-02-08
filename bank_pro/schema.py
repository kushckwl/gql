import graphene
import bank.schema 


class Query(bank.schema.Query, graphene.ObjectType):
    pass  
       

schema = graphene.Schema(query=Query)        