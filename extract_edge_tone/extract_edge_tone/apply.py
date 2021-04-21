import os


def move_files(nm):
    for x in nm:
            os.system(f'cp "data/input_batch/{x}" data/input')



def remove_files(nm):
    for x in nm:
            os.system(f'rm "data/input/{x}"')



remove_files(os.listdir('data/input'))
remove_files(os.listdir('data/edge_tone'))

f = os.listdir('data/input_batch')
L = len(f)

BATCH = 20

print(f'length is {L} and batch is {BATCH}')



for i in range(L//BATCH):
	print(f'running lap {i}')
	localnames = f[BATCH*i:BATCH*(i+1)]
	move_files(localnames)
	os.system('matlab -nodisplay -r "try Im2Pencil_get_edge_tone ; catch fprintf(\'err!\'); end ; quit()"')
	remove_files(localnames)

