from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, Proveedores

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'rol']
        extra_kwargs = {
            'password': {'write_only': True},  # Para que no se muestre la contraseña al serializar
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)

            if user:
                if not user.is_active:
                    msg = 'El usuario está desactivado.'
                    raise serializers.ValidationError(msg)
            
            else:
                msg = 'No se pudo iniciar sesión con las credenciales proporcionadas.'
                raise serializers.ValidationError(msg)
        
        else:
            msg = 'Debe proporcionar email y contraseña.'
            raise serializers.ValidationError(msg)
        
        data['user'] = user
        return data
    
class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'