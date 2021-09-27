from django.core.mail import EmailMessage
from django.conf import settings

if not settings.configured:
    settings.configure()


def SendEmail(UserData):
    """
    :param UserData: Serialized and validated response recorded in the form (Type = Dictionary)
    :return: Sends Confirmation email
    """
    Name = UserData['name']
    BirthDate = UserData['birth']
    EmailID = UserData['email']
    Phone = UserData['phone']

    Subject = f"{Name} Your Submission Details"

    Text_Message = f"Dear {Name} your form was submitted successfully\n" \
                   f"Please verify your details\n" \
                   f"Name : {Name}\n" \
                   f"Birthday : {str(BirthDate)}" \
                   f"EmailID : {EmailID}\n" \
                   f"Phone : {Phone}"

    Email = EmailMessage(subject=Subject, body=Text_Message, from_email=EMAIL_HOST_USER, to=[EmailID])
    Email.send(fail_silently=False)
