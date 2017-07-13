class MainControl:
    def __init__(self,opt):
        self.opt = opt


    def selection(self):
        if self.opt == 1:
            print ("1. Create a new blog post:")
            print (obj.blogpost())

        elif self.opt == 2:
            print ("2. Retrieve the Content based on Title:")
            print (obj.content())

        else:
            print ("")

class BlogPost(MainControl):
    def __init__(self,opt):
        MainControl.__init__(self,opt)

    #for updating the blog data in dictionary
    def blogpost(self):
        a = raw_input("Enter a Title")
        b = raw_input("Enter the content")
        blog[a]=b

    #for retrieving the content
    def content(self):
        index = 1
        for key in blog:
            print ("%s. %s"%(index, key))
            index += 1

        try:
            option = input("Select an title: ")
            option = int(option)
            if ((option >= index) or (option == 0)):
                print ("Enter a valid input")
                return (obj.selection())
            else:
                print (blog.values()[(option-1)])
        except NameError:
            print ("Enter a valid numeric input")
            return (obj.selection())


blog = {}

while True:
    opt = int(input("Select an Option \n 1. Create a new blog post \n 2. Retrieve the content by selecting the title \n 3. Selecting the option again \n"))

    obj = BlogPost(opt)

    obj.selection()
