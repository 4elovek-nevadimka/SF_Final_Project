from rest_framework import serializers

from silant.models import Machine, Claim, Maintenance


# class MachineSerializer(serializers.HyperlinkedModelSerializer):
class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'
        # fields = ['url', 'serial_number']


# class MaintenanceSerializer(serializers.HyperlinkedModelSerializer):
class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'
        # fields = ['url', 'maintenance_type']


# class ClaimSerializer(serializers.HyperlinkedModelSerializer):
class ClaimSerializer(serializers.ModelSerializer):
    # machine = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='machine-detail')

    class Meta:
        model = Claim
        fields = '__all__'
        # fields = ['url', 'failure_date', 'operating_time', 'failure_description', 'machine']
