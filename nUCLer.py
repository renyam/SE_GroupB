class User:

    _all_users = []

    def __init__(self, name):
        """
        Constructor of the user class
        Parameters: name
        Returns: an instance of the class User
        """
        self._name = name
        self._type=None
        self._information = []
        self._email = None
        self._password = None
        self._status=False


        User._all_users.append(self) 

    def get_name(self):
        return self._name

    def set_name(self, name):
        """
        We need to make sure that name is a string
        """
        assert isinstance(name, str)
        self._name = name

    def changeUserInformation(tp,email,password):
        self._type=tp
        self._email=email
        self._password=password
        _information.append(tp,email,password)

    def get_userInformation(self):
        return self._information

    def get_login(self):
        self._status=True


class Forum():

    def _init_(self):
        _forum_list = []
        _forum_description = []
        

    def search_post(self):
        self.counter = 0
        if _forum_list = [counter] and counter < len._forum_list[]:
            print (_forum_list[counter], _forum_description[counter])

        else if counter >= len._forum_list[]:
            print ("The post has not been found")

        else:
            counter = counter + 1

    def addPost(name, description, content):
        self._froum_list.append(name)
        self._froum_desciption.append(description)
        self._forum_content.append(content)

    def deletePost(name):
        print ("Do you want to delete the post with post name: " + name)
        
        self.counter = 0
        if _forum_list == [counter] and counter < len._forum_list[]:
            del _froum_list[counter]
            del _forum_description[counter]
            del _forum_content[counter]

        else if counter >= len._forum_list[]:
            print ("The post has not been found")

        else:
            counter = counter + 1
            
        
class Post(Forum):

    def _init_(self):
        super._init_()
        self.reply_to_post = []
        _post_content= []
        
        self._like = 0
        self._forward = 0


    def viewPost(self):
        print (_forum_list, _forum_description, _post_content, _reply_to_post, _like, _forward)

    def replyPost(reply):
        self.reply_to_post.append(reply)

    def likePost(self):
        _like = _like + 1

    def forwardPost(self):
        _forward = _forward + 1

    def subscribe(self):
        postSubscribed()
    





class ChatList():

    def _init_(self):
        self._student_list = []
        self._student_year = []
        self._student_infor = []
        self._partial_chat_history = []
        print (_student_list[], _student_year[], _student_infor[], _partial_chat_history[])

    def viewChat():
        print(_student_list, _student_basic_infor,_partial_chat_history)

    def search_student(student_name,year):
        self.counter = 0
        if student_name == _student_list[counter] and year == _student_year[counter]:
            print (_student_list[counter], _student_year[counter], _student_infor[counter])

        else if counter > len._student_list:
            print("student not found")

        else:
            counter = counter + 1

    def chat():
        
        Chatroom._messageTo()


class ChatRoom(Chatlist):

    def _init(self):
        self._chat_content=[]
        self._student_name = []

    def _messageTo(message):
        return message


class Attendence():

    def _init_(self):
        self._instruction = ("Please scan the QR code")
        self._module = [DB, SE, BRM]
        self._total_lessons = 10
        self._attended_lessons = [0,0,0]
        

    def scanQrCode(module,_attended_lessons):
        print(_instruction)
        _attended_lessons = _attended_lessons + 1
        self.counter = 1
        if module == _module[counter] and counter < len._module[]:
            _attended_lessons[counter] = _attended_lessons
            print("Attendence has been taken")

        else if counter > len.module[]:
            print("Module has not been found")

        else:
            counter = counter + 1

    def flashlight():
        turnOnFlashLight()

    def tapOnRecord():
        self.counter = 0
        if counter < len.module:
            print(_module[counter])
            print(_attended_lessons/_total_lessons)

        else if counter > len.module[]:
            break

        else:
            counter = counter + 1


    def reportIssue(issue):
        issueReported()



class Notification(Post):

    def _init_(self):
        self._notification = "you have an update from your subscribed post"

    def _noticication(self):
        print(_notification)

    def viewPost(self):
        super.viewPost()

    def unsubscribe(self):
        postUnsubscribed()

        
        

















    

