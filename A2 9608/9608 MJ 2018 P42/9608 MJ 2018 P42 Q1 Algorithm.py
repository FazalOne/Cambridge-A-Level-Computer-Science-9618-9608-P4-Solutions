while NewCollection != "No":
    while AddPhoto != "No":
        TakePhoto()
        AddPhotoToCollection(AddPhoto)
        AddPhoto = input("Do you want to take another photo?")
    while NewUser != "No":
        AddUser(NewUser)
        NewUser = input("Do you want to add another user?")
    NewCollection = input("Do you want to create another collection?")