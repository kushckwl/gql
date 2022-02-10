import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from .models import Bank, Branches
from graphene_django.filter import DjangoFilterConnectionField


class BankNode(DjangoObjectType):
    class Meta:
        model = Bank
        filter_fields = ['name', 'id']
        interfaces = (relay.Node, )



class BranchesNode(DjangoObjectType):
    class Meta:
        model = Branches
        filter_fields = ['ifsc','bank_id','branch','address','city','district','state']     
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    bank = DjangoFilterConnectionField(BankNode)
    branches = DjangoFilterConnectionField(BranchesNode)


  

schema = graphene.Schema(query=Query)        