class CustomerRecord:
    def __init__(self, username, password):
        self.Username = username #STRING
        self.Password = password #STRING

CustomerLogIn = [CustomerRecord("", "") for _ in range(3000)] #ARRAY OF CustomerRecord

def SearchHashTable(SearchUser):
    index = hash(SearchUser) #INTEGER
    count = 0 #INTEGER

    while (CustomerLogIn[index].Username != SearchUser and CustomerLogIn[index].Username != '' and count < 2999):
        index += 1
        count += 1
        if index > 2999:
            index = 0
    if CustomerLogIn[index].Username == SearchUser:
        return index
    else:
        return -1