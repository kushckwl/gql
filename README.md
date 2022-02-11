# GraphQL

### Live at https://indbank.herokuapp.com/gql

## Api Documentation

#### This project made in Django Framework. I used graphene library to make this project. Project live at https://indbank.herokuapp.com/gql

Query
```   
query{
  branches{
    edges{
      node{
        branch
        bankId{
          name
        }
        ifsc
        }
      }
    }
  }
```
Output
```
{
  "data": {
    "branches": {
      "edges": [
        {
          "node": {
            "branch": "STATE BANK OF BIKANER AND JAIPUR",
            "bankId": {
              "name": "STATE BANK OF INDIA"
            },
            "ifsc": "SBBJ0011297"
          }
        },
        {
          "node": {
            "branch": "PUNJAB NATIONAL BANK",
            "bankId": {
              "name": "PUNJAB NATIONAL BANK"
            },
            "ifsc": "PUNB0356800"
          }
        }
      ]
    }
  }
}
```
