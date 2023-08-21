from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from user.models import Move, AppUser
from user.serializers import MoveSerializer
from rest_framework.views import APIView
from django.db.models import Q


@api_view(['POST'])
def create_move(request):
    from_user_id = request.data.get('from')
    to_user_id = request.data.get('to')
    coins = request.data.get('coins')

    from_user = AppUser.objects.get(pk=from_user_id)
    to_user = AppUser.objects.get(pk=to_user_id)

    print(from_user,to_user)
    if from_user.coins < coins:
        return Response({'error': 'Insufficient coins.'}, status=status.HTTP_400_BAD_REQUEST)

    move = Move.objects.create(from_user=from_user, to_user=to_user, coins=coins)
    
    # Update coins for from_user and to_user
    from_user.coins -= coins
    to_user.coins += coins
    from_user.save()
    to_user.save()

    # Add the new move to the moves ManyToMany fields of both users
    # from_user.moves_related.add(move)
    # to_user.moves_related.add(move)

    return Response(MoveSerializer(move).data, status=status.HTTP_201_CREATED)

class MoveListView(APIView):
    def get(self, request, user_id):

        moves = Move.objects.filter(Q(from_user_id=user_id) | Q(to_user_id=user_id))
        serializer = MoveSerializer(moves, many=True) 
        return Response(serializer.data)