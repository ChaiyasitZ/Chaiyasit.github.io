import networkx as nx
import matplotlib.pyplot as plt

network = nx.Graph()
provinces = ['Chumphon', 'Krabi', 'Nakhon Si', 'Narathiwat', 'Pattani', 'Phang Nga', 
             'Phatthalung', 'Phuket', 'Ranong', 'Satun', 'Songkhla', 'Surat Thani', 'Trang', 'Yala']

pos = {'Chumphon': (1, 15), 
       'Krabi': (2, 5), 
       'Nakhon Si': (3, 10), 
       'Narathiwat': (6, 0),
       'Pattani': (6, 5), 
       'Phang Nga': (1, 5), 
       'Phatthalung': (4, 5), 
       'Phuket': (1, 0), 
       'Ranong': (1, 10), 
       'Satun': (3, 0), 
       'Songkhla': (5, 5), 
       'Surat Thani': (2, 10), 
       'Trang': (3, 5), 
       'Yala': (5, 0)}

network.add_nodes_from(provinces)
print(f"There are {network.number_of_nodes()} provinces in total.")

network.add_edge('Chumphon', 'Ranong')
network.add_edge('Chumphon', 'Surat Thani')
network.add_edge('Krabi', 'Phang Nga')
network.add_edge('Ranong', 'Phang Nga')
network.add_edge('Ranong', 'Surat Thani')
network.add_edge('Surat Thani', 'Krabi')
network.add_edge('Surat Thani', 'Nakhon Si')
network.add_edge('Surat Thani', 'Phang Nga')
network.add_edge('Krabi', 'Trang')
network.add_edge('Krabi', 'Nakhon Si')
network.add_edge('Trang', 'Nakhon Si')
network.add_edge('Phatthalung', 'Nakhon Si')
network.add_edge('Songkhla', 'Nakhon Si')
network.add_edge('Trang', 'Satun')
network.add_edge('Phatthalung', 'Satun')
network.add_edge('Trang', 'Phatthalung')
network.add_edge('Phatthalung', 'Songkhla')
network.add_edge('Songkhla', 'Pattani')
network.add_edge('Pattani', 'Narathiwat')
network.add_edge('Pattani', 'Yala')
network.add_edge('Narathiwat', 'Yala')
network.add_edge('Yala', 'Songkhla')
network.add_edge('Songkhla', 'Satun')
network.add_edge('Phuket', 'Phang Nga')

edge_labels = {('Chumphon', 'Ranong'): '121.2 km',
               ('Chumphon', 'Surat Thani'): '217.8 km',
               ('Krabi', 'Phang Nga'): '145.7 km',
               ('Ranong', 'Phang Nga'): '212.3 km',
               ('Ranong', 'Surat Thani'): '240.2 km',
               ('Surat Thani', 'Krabi'): '120.9 km',
               ('Surat Thani', 'Nakhon Si'): '137.7 km',
               ('Surat Thani', 'Phang Nga'): '115.6 km',
               ('Krabi', 'Trang'): '115.6 km',
               ('Krabi', 'Nakhon Si'): '107.1 km', 
               ('Trang', 'Nakhon Si'): '141.0 km', 
               ('Phatthalung', 'Nakhon Si'): '154.8 km',
               ('Songkhla', 'Nakhon Si'): '252.1 km',
               ('Trang', 'Satun'): '117.3 km',
               ('Phatthalung', 'Satun'): '123.7 km',
               ('Trang', 'Phatthalung'): '49.6 km',
               ('Phatthalung', 'Songkhla'): '124.1 km',
               ('Songkhla', 'Pattani'): '109.2 km',
               ('Pattani', 'Narathiwat'): '115.9 km',
               ('Pattani', 'Yala'): '90.3 km',
               ('Narathiwat', 'Yala'): '103.0 km',
               ('Yala', 'Songkhla'): '173.7 km',
               ('Songkhla', 'Satun'): '108.1 km',
               ('Phuket', 'Phang Nga'): '108.3 km'}
              
color_dict = {'Chumphon': '#15B01A', 
              'Krabi': '#E50000', 
              'Nakhon Si': '#FF7D40', 
              'Narathiwat': '#008000',
              'Pattani': '#00EEEE', 
              'Phang Nga': '#00FFFF', 
              'Phatthalung': '#66CD00', 
              'Phuket': '#1C86EE', 
              'Ranong': '#FAC205', 
              'Satun': '#FF00FF', 
              'Songkhla': '#6495ED', 
              'Surat Thani': '#1E90FF', 
              'Trang': '#BF3EFF', 
              'Yala': '#A9A9A9'}

colors = [color_dict[node] for node in network.nodes()]
sizes = [5678] * len(network.nodes())

plt.figure(figsize=(20, 16))
plt.title("Distance of each province in Southern Thailand", size=20)
nx.draw_networkx(network, pos=pos, node_color=colors, node_size=sizes, with_labels=True, font_size=11, linewidths=0.5, font_color='black', font_weight='700')
nx.draw_networkx_edge_labels(network, pos=pos, edge_labels=edge_labels, font_size=9, font_color='black', label_pos=0.5, rotate=False)
plt.show()
          
              