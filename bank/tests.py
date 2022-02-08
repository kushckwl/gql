from bank.schema import Query
from django.test.testcases import TestCase
from graphene import Schema
import graphene

class AnExampleTest(TestCase):

    def setUp(self):
        super().setUp()
        self.query = """
            query{
               bank{
                   edges{
                      node{
                         id
                      }
                   }
    
                 }

             }
 
        """

    def test_an_example(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertDictEqual({"bank": {"id": "QmFua05vZGU6MQ=="}}, result.data)