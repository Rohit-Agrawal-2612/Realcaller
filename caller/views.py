from django.shortcuts import render
from caller.models import MyUser, UnauthUsers
from django.http import JsonResponse
from caller.serializers import MyUserSerializer, UnauthUsersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search(request):
    if request.method == 'POST':
        name = request.data.get('name',None)
        phone_number = request.data.get('phone_number',None)
        if name is not None:
            Authuser1 = MyUser.objects.filter(name__startswith=name)
            Unauthuser1 = UnauthUsers.objects.filter(name__startswith=name)
            Authuser2 = MyUser.objects.filter(name__icontains=name)
            Unauthuser2 = UnauthUsers.objects.filter(name__icontains=name)
            Authuser1.union(Authuser2)
            Unauthuser1.union(Unauthuser2)
            Serializer1 = MyUserSerializer(Authuser1, many=True)
            Serializer2 = UnauthUsersSerializer(Unauthuser1, many=True)

        elif phone_number is not None:
            user1 = MyUser.objects.filter(phone_number=phone_number)
            user2 = UnauthUsers.objects.filter(phone_number=phone_number)
            if len(user1) == 1:
                Serializer = MyUserSerializer(user1, many=True)
                return JsonResponse({"Authenticated":Serializer.data})
            elif len(user2) == 1:
                Serializer = UnauthUsersSerializer(user2, many=True)
                return JsonResponse({"Unauthenticated":Serializer.data})
            else:
                user1 = MyUser.objects.filter(phone_number__contains=phone_number)
                user2 = UnauthUsers.objects.filter(phone_number__contains=phone_number)
                Serializer1 = MyUserSerializer(user1, many=True)
                Serializer2 = UnauthUsersSerializer(user2, many=True)
        else:
            users1 = MyUser.objects.all()
            users2 = UnauthUsers.objects.all()
            Serializer1 = MyUserSerializer(users1, many=True)
            Serializer2 = UnauthUsersSerializer(users2, many=True)
        return JsonResponse({"Authenticated":Serializer1.data,"Unauthenticated":Serializer2.data})

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        number = request.data['phone_number']
        user = UnauthUsers.objects.filter(phone_number=number)
        if len(user) > 0:
            user[0].delete()
        Serializer = MyUserSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse({"message" : "user created successfully!!"})
        else:
            return JsonResponse({"errors":Serializer.errors})

@api_view(['POST'])    
@permission_classes([IsAuthenticated])
def spam(request):
    if request.method == 'POST':
        number = request.data['phone_number']
        user1 = MyUser.objects.filter(phone_number=number)
        if len(user1) == 0:
            user2 = UnauthUsers.objects.filter(phone_number=number)
            if len(user2) != 0:
                user2[0].spam_count += 1
                user2[0].save()
                return JsonResponse({"message":"marked as spam successfully!!"})
        else:
            user1[0].spam_count += 1
            user1[0].save()
            return JsonResponse({"message":"marked as spam successfully!!"})
        return JsonResponse({"message":"number not found!!"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def contacts(request):
    if request.method == 'POST':
        data = request.data.get('contacts',None)
        for objs in data:
            obj = MyUser.objects.filter(phone_number=objs['phone_number'])
            if len(obj) == 0:
                obj = UnauthUsers.objects.filter(phone_number=objs['phone_number'])
                if len(obj) == 0:
                    user = UnauthUsers(name=objs['name'], phone_number=objs['phone_number'])
                    user.save()
        return JsonResponse({"message":"contacts stored successfully!!"})
