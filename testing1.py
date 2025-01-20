import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[:4:2])
# ndum is the dimension of the array
#arr.reshape(4,3) reshapes the array to 4 arrays with three elements
#np.concatenate((arr1, arr2))
#axis=0 is the row. axis=1 is the column
import os
cwd= os.getcwd()
print(cwd)
# os.mkdir() Used to create a directory named path with the specific numeric mode.
print(os.listdir()) # THis list the files in the current directory. The current directory is VSCode Project
#os.remove() used to remove or delete a file path/ It doesn't delete a directry
print("Below is the name")
print(os.name)
# pathlib is way to work with files and interact with the file system
from pathlib import Path
print(1)
print(Path.cwd()) # This also returns the cwd
print(Path.cwd().parent) # Index i returns the i'th parent
# We can join path by using shash
cwd = Path.cwd()
join_path = cwd/'Hello' # This directly join the path. This is good!
join_path.mkdir(exist_ok=True) # Note that this creates a directory
# We can cha
path = Path(r"C:\Users\baiyu\Desktop") # Note that we need to put r 
new_path = path/"bruh" # We can directlt create a path by calling the path method
print(new_path)
# We check whether a specific dir exist by using the joined_path.is_dir() method
# Pathlib makes it easy to iterate the directories
#e.g. for file in target_dir.itedir(): if file.suffix ==".text" print(file)
print(2)
# '..' represents the parent directory. We can replace .. by ../ and the code still works
# The code first make a directory that joihj the parent of cwd and data/ let exist tryue to be pk
# data file is to joij three files and put the house_tiny.csv into data
# with open(data_file, w') as f: f.write() willl write things in the
# We then import pd to read the csv. file and it's nice
# data preparation. Un supevise learning we train modes to predict the target value given input
#in pandas pd.iloc[:,0:2] give the thing in the corresponding integer coordinates. 
# For missing numerical values we replace thenm with NaN with the corresponding column. sum(axis=0) returns the sum from the rows. 
# Elementwise product for pytorch tensor is performed by *
# DOt product ius performed by torch.dot(x,y)
# Matrix product is performed by @ or torch.mm
# torch.norm(u) retruns the nrom of the vector with the l2 form 
# We then want to consider how to get the differentials. Watch video for this one
#plt.plot(x, y, 'x', 'y', legend=things)
# Learn how autograd works
#x = torch.arange(4.0, requires_grad=True). x.grad is None by default
# We can perform gradient of y with respect to x by calling the backward methid and 
#pytorch doesnt automatically reset the gradinet uffer when record a new gradient. need to call grad.zero()
# Use the method detach to turn off autograd
# For autograd it keepos track of the operation
#e.g x = torch.tensor(2.0, requires_grad=True)
# y = x**2+3x+1
#y.backward()
#x.grad returns the corresponding gradient values