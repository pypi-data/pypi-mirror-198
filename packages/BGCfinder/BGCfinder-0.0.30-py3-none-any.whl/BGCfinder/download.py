import os
import requests

def download():
	print('Download starts ...')
	def absolute_pwd(file_name):
		return os.path.join(os.path.dirname(__file__), file_name)
		
	pwd = absolute_pwd('')

	if not os.path.exists(absolute_pwd('model')):
		os.makedirs(absolute_pwd('model'))
		
	if not os.path.exists(absolute_pwd('data')):
		os.makedirs(absolute_pwd('data'))
		
	# download checkpoint file
	MODEL_VERSION = '0.0.1'
	
	url = 'https://docs.google.com/uc?export=download&id=1uJwhNF3WDsKUoRLUFejAPxLpQyvxfAgG' #GCN
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('model/BGCfinder_model_checkpoint_GCN_' + MODEL_VERSION), 'wb').write(r.content)
	
	url = 'https://docs.google.com/uc?export=download&id=1C5_5NihgVLmeuX7EW1lNe7tmamFCI-rp' #GraphSAGE
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('model/BGCfinder_model_checkpoint_GraphSAGE_' + MODEL_VERSION), 'wb').write(r.content)
	
	url = 'https://docs.google.com/uc?export=download&id=1wTCcz4Uq8JtXfK57iNeZdwtUHeB_7h5N' #GAT
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('model/BGCfinder_model_checkpoint_GAT_' + MODEL_VERSION), 'wb').write(r.content)
	
	url = 'https://docs.google.com/uc?export=download&id=1jeAuUFy-ltA6e_RIPYH8RaaW9D07hJcM' #GIN
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('model/BGCfinder_model_checkpoint_GIN_' + MODEL_VERSION), 'wb').write(r.content)
	
	url = 'https://docs.google.com/uc?export=download&id=1R42l-os9KlI1UJkwudEtvmwfJf6d3fPg' #GINE
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('model/BGCfinder_model_checkpoint_GINE_' + MODEL_VERSION), 'wb').write(r.content)

	# download example files
	url = 'https://docs.google.com/uc?export=download&id=1I_Px_oKyRmx9gRNhDnqwyM5s1VAw6shR'
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('data/input_example_1.fasta'), 'wb').write(r.content)

	url = 'https://docs.google.com/uc?export=download&id=1jsnuKCM_tnpFLxiblM4TVRqeDbRAoUuG'
	r = requests.get(url, allow_redirects=True)
	open(absolute_pwd('data/input_example_2.fasta'), 'wb').write(r.content)

	print('Download finish')
