MVP for the paytastic hackaton. send a POST request, get the best option for your transaction. admin forms to define the various quotes (read-only) and a log of all the past transactions (read only too)

data structure expected by the api:
    


TODO:
 - create js (react? nah.) script for website inclusion
    - inject form
    - on click, call the ashwort api, update form to show 'in progress'
    - on successfull callback, update the form with a success
    
 - create the api for the custom script
    - api endpoint
    - 3rd party api integration (mastercard, may something more)
    - auth
    
 - extra: expand to take into account the foreign currency fee
    - grab as a parameter the currency
    - ping xignite to check the mid market rate
    - do some magic and decide which is the best option
    
 - improve: move quote logic to queryset, not view
 
 - extra extra: more robust error and security handling
 
 - extra extra extra: make coffee
 
 
 Code by Lorenzo Turrino
