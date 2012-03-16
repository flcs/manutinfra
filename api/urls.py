from django.conf.urls.defaults import *
from piston.resource import Resource
from manutinfra.api.handlers import Handler_Manutencao , Handler_Infra , Handler_Manutencao_ID , Handler_Infra_ID , Handler_Infra_Aprovacao , Handler_Manutencao_Aprovacao

#class CsrfExemptResource( Resource ):
#	def __init__( self, handler, authentication = None ):
#		super( CsrfExemptResource, self ).__init__( handler, authentication )
#		self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )


manutencao_resource = Resource(Handler_Manutencao)
manutencao_id_resource = Resource(Handler_Manutencao_ID)
manutencao_aprov_resource = Resource(Handler_Manutencao_Aprovacao)

infra_resource = Resource(Handler_Infra)
infra_id_resource = Resource(Handler_Infra_ID)
infra_aprov_resource = Resource(Handler_Infra_Aprovacao)

urlpatterns = patterns('',
#	url(r'ordens_manutencao/(?P<emitter_format>.+)/$',manutencao_resource),
	(r'ordens_manutencao/$',manutencao_resource),
	(r'ordens_manutencao/(?P<ordem_id>\d+)$', manutencao_id_resource),
	(r'ordens_manutencao/aprovacao',manutencao_aprov_resource),
	(r'ordens_infraestrutura/$',infra_resource),
	(r'ordens_infraestrutura/(?P<ordem_id>\d+)$', infra_id_resource),
	(r'ordens_infraestrutura/aprovacao',infra_aprov_resource),
)
