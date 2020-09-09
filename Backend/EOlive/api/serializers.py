from rest_framework import serializers
from rest_framework.authtoken.models import Token
from EOlive.models import User, evidencijagospodarstva, berba, podaci_radnje, prihranjivanje, spricanje

class userSerializer(serializers.Serializer):
    id = serializers.IntegerField(write_only=True)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128)
    is_active = serializers.BooleanField(default=True)
    is_admin = serializers.BooleanField(default=False)
    # is called if we save serializer if it do not have an instance
    def create(self, validated_data):
       password = validated_data.pop("password")
       user = User.objects.create(**validated_data)
       if password:
           user.set_password(password)
           user.save()
       return user
    # is called if we save serializer if it have an instance
    def update(self, instance, validated_data):
       password = validated_data.pop("password")
       instance.__dict__.update(validated_data)
       if password:
           instance.set_password(password)
       instance.save()
       return instance

class TokenSerializer(serializers.ModelSerializer):

    def get_user(self, obj):
        User = self.context['request'].user.id
        print(User)
        return User

    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = Token
        fields = ('key', 'user') 

class evidencijagospodarstvaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = evidencijagospodarstva
        fields = ('katastar', 'naselje', 'povrsina', 'naziv_gosp', 'User_id', 'user')

    def get_user(self, obj):
        User = self.context['request'].user.id
        print(User)
        return User

        


class berbaSerializer(serializers.ModelSerializer):

    naziv_gosp = serializers.SerializerMethodField('get_opg')

    class Meta:
        model= berba
        fields = ('id', 'vrstamaslina', 'datumb', 'katcest', 'kolicinaubrano', 'doprinosulja', 'naziv_gosp')

    def get_opg(self, EOlive):
        naziv_gosp = EOlive.User.naziv_gosp
        return naziv_gosp

class podaci_radnjeSerializer(serializers.ModelSerializer):

    naziv_gosp = serializers. SerializerMethodField('get_gosp')

    class Meta:
        model= podaci_radnje
        fields = ('id', 'vrstaradnje', 'katcest', 'datum', 'naziv_gosp')

    def get_gosp(self, EOlive): 
        naziv_gosp = EOlive.User.naziv_gosp
        return naziv_gosp

class prihranjivanjeSerializer(serializers.ModelSerializer):

    vrstaradnje = serializers. SerializerMethodField('get_radnja')

    class Meta:
        model= prihranjivanje
        fields = ('id', 'nazivprihrane', 'kolicinap', 'katcest', 'datump', 'vrstaradnje')

    def get_radnja(self, EOlive): 
        vrstaradnje = EOlive.User.vrstaradnje
        return vrstaradnje

class spricanjeSerializer(serializers.ModelSerializer):

    vrstaradnje = serializers. SerializerMethodField('get_rad')

    class Meta:
        model= spricanje
        fields = ('id', 'nazivtek', 'kolicina', 'katcest', 'datums', 'vrstaradnje')

    def get_rad(self, EOlive): 
        vrstaradnje = EOlive.User.vrstaradnje
        return vrstaradnje

