from django.shortcuts import redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.shortcuts import redirect

from . models import AlertsBody, Account, Agent, Profile, Comment
from . serializers import UserCreateSerializer, AlertsBodySerializer, AccountSerializer, AgentSerializer, ProfileSerializer, CommentSerializer



#------------------------

# class LoginAfterPasswordChangeView(PasswordChangeView):
#     @property
#     def success_url(self):
#         return reverse_lazy('account_login')
#
# login_after_password_change = login_required(LoginAfterPasswordChangeView.as_view())

#-------------------------

# class RedirectToPage(redirect('login')):
#     def redirect_view(request):
#         response = redirect('/redirect-success/')
#         return response

#-----------------------

# class RedirectToPage(redirect()):
#     def redirect_view(request):
#         response = redirect ('/redirect-success/')
#         return response

#--------------------------

class RegisterUser(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            data_to_return = {}
            data_to_return['id'] = serializer.data['id']
            data_to_return['username'] = serializer.data['username']
            data_to_return['first_name'] = serializer.data['first_name']
            data_to_return['last_name'] = serializer.data['last_name']
            data_to_return['email'] = serializer.data['email']
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(data_to_return, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#------------------------


class AlertsBodiesList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        alerts_bodies = AlertsBody.objects.all()
        serializer = AlertsBodySerializer(alerts_bodies, many=True) # serializes!!!
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AlertsBodySerializer(data=request.data) # data=request.data -> deserializes!!!

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AccountsList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True) # serializes!!!
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)# data=request.data -> deserializes!!!

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AgentsList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AgentSerializer (data=request.data)  # data=request.data -> deserializes!!!

        if serializer.is_valid ():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentsList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)  # data=request.data -> deserializes!!!

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#------------------------


class AlertsBodyDetails(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            alerts_body = AlertsBody.objects.get(pk=pk)
            return alerts_body
        except AlertsBody.DoesNotExist:
            raise Http404

    def get(self, request, alerts_body_id):
        alerts_body = self.get_object(pk=alerts_body_id)
        serializer = AlertsBodySerializer(alerts_body)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, alerts_body_id):
        alerts_body = self.get_object(pk=alerts_body_id)
        serializer = AlertsBodySerializer(alerts_body, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, alerts_body_id):
        alerts_body = self.get_object(pk=alerts_body_id)
        alerts_body.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AccountDetails(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            account = Account.objects.get(pk=pk)
            return account
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, account_id):
        account = self.get_object (pk=account_id)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, account_id):
        account = self.get_object(pk=account_id)
        serializer = AccountSerializer(account, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, account_id):
        account = self.get_object(pk=account_id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AgentDetails(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            agent = Agent.objects.get(pk=pk)
            return agent
        except Agent.DoesNotExist:
            raise Http404

    def get(self, request, agent_id):
        agent = self.get_object(pk=agent_id)
        serializer = AgentSerializer(agent)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, agent_id):
        agent = self.get_object(pk=agent_id)
        serializer = AgentSerializer(agent, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, agent_id):
        agent = self.get_object(pk=agent_id)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CommentDetails(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            return comment
        except Comment.DoesNotExist:
            raise Http404

    # def get(self, request, alerts_body_id, comment_id): #pk = AlertBody pk
    #     full_request_url = request.build_absolute_uri()



#------------------------

class UserList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'alerts_bodies': reverse('alerts-bodies', request=request, format=format),
        'accounts': reverse('accounts', request=request, format=format),
        'agents': reverse('agents', request=request, format=format),
        'comments': reverse('comments', request=request, format=format),

    })

