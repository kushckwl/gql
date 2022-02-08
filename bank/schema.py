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
    #all_bank = relay.Node.Field(BankNode)
    bank = DjangoFilterConnectionField(BankNode)
    # all_branches = relay.Node.Field(BranchesNode) 
    branches = DjangoFilterConnectionField(BranchesNode)


    # def resolve_bank(root, info):
    #     return Bank.objects.all() 

    # def resolve_branches(root, info):
    #     return Branches.objects.all()    
       

schema = graphene.Schema(query=Query)        