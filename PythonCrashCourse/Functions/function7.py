def describe_pet(animal_type="Cat",pet_name="Lexi"):
    print("\bI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet(animal_type="Hamster",pet_name="Harry")
describe_pet(pet_name="Willie",animal_type="Dog")
describe_pet(pet_name="Lucy")
describe_pet()