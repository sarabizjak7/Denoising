import sys

import numpy
import imageio

import copy

# OPIS POSTOPKA
# Preberem ime vhodne in izhodne slike
# Odprem vhodno sliko kot numpy array4
# Naredim kopijo vhodne slike
# Za vsak piksel p:
#  - * Izracunam njegovo k-"okolico" B_k(p) --- shranim jo v nek seznam (ali numpy array)
#  - * Izracunam mediano elementov tega seznama m
#  - V novi sliki piksel p prepisem z mediano elementov njegove k-okolice m
# Shranim novo sliko z ustreznim imenom


def get_neighborhood(I, i, j, k):
	
	w, h, _ = I.shape
	
	seznam_okolice = []
	
	for idx in range(i - k, i + k):
		for jdx in range(j - k, j + k):
			#kdaj smo izven slike
			
			if idx < 0 or idx > w - 1 or jdx < 0 or jdx > h - 1:
				continue
			
			seznam_okolice.append((idx, jdx))
			
	return seznam_okolice	
	
	
def get_rgb_neighborhood(I, i, j):
	
	okolica1 = get_neighborhood(I, i, j, 3)
	rgb_okolica = []
	
	for element in okolica1:
		rgb = list(I[element])
		rgb_okolica.append(rgb)
	
	return rgb_okolica
		

			
def get_geometric_median(I, i, j):

	r_okolica = []
	g_okolica = []
	b_okolica = []
	
	okolica2 = get_rgb_neighborhood(I, i, j)
	for element in okolica2:
		r_okolica.append(element[0])
		g_okolica.append(element[1])
		b_okolica.append(element[2])
		
	r_okolica.sort()
	g_okolica.sort()
	b_okolica.sort()
	
	r = len(r_okolica)
	g = len(g_okolica)
	b = len(b_okolica)
	
	if r % 2 == 0:
		prvi = r // 2 - 1
		drugi = r // 2
		r_average = float((int(r_okolica[prvi]) + int(r_okolica[drugi])) / 2)
	else:
		r_average = float(r_okolica[r // 2])
		
	if g % 2 == 0:
		prvi = g // 2 - 1
		drugi = g // 2
		g_average = float((int(g_okolica[prvi]) + int(g_okolica[drugi])) / 2)
	else:
		g_average = float(g_okolica[g // 2])
		
	if b % 2 == 0:
		prvi = b // 2 - 1
		drugi = b // 2
		b_average = float((int(b_okolica[prvi]) + int(b_okolica[drugi])) / 2)
	else:
		b_average = float(b_okolica[b // 2])
		
		
	return [r_average, g_average, b_average]

	
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Uporaba: python main.py vhodna izhodna")
		sys.exit(1)

	infile = sys.argv[1]
	I = imageio.imread(infile)

	w, h, _ = I.shape
	

	for i in range(w):
		for j in range(h):
			#print((i, j), " -> ", I[i, j])
			#okolica = get_neighborhood(I, i, j, 3)
			#print(okolica)
			#rgb = get_rgb_neighborhood(I, i, j)
			#print(rgb)
			mediana = get_geometric_median(I, i, j)
			print(mediana)
			
			
			
			
	#print("Dimenzije slike: ", I.shape)		
			