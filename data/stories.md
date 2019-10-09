## happy path
* greet
  - utter_greet

## moody
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet

## moody1
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help

## moody2
* affirm
  - utter_happy

## say goodbye
* goodbye
  - utter_goodbye

## register form story
* register_request
    - register_form
    - form{"name":"register_form"}
    - form{"name":"null"}
    - utter_slot_values
