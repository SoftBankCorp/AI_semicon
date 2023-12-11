#two way to start process
# spawn method, fork method
#1) spawn method: create process with code
#2) fork method: create parent process with dupulicate, it construct process fastly
           #but, on dupulicating, code of memory and amount of data are duplicated at the same time

# import multiprocessing
# def start_process():
#     return 1

# ##maincode part
# if __name__=='__main__':
#     p1=multiprocessing.Process(target=start_process)
#     p1.start()
    
#     print(multiprocessing.get_start_method()) ##spawn method
#     #this time python has windows os, so use default value spawn method , making process
#     ## linux case: fork method is default,to set spawn,            ~
    
################
#create many process and start them
import multiprocessing as mp ##nickname as

def worker_process(name):
    ##define  work of  each process
    print(f"Worker process {name} started")
    ##print that staring each process
        
if __name__ =='__main__':
    num_processes = 4 # specify 
    #process list
    processes = []
    
    # Construct and start multiprocess
    for i  in range(num_processes):
        p=mp.Process(target=worker_process,args=(i,))
        p.start()
        processes.append(p)
        
    for i in processes:
        i.join()
        
    print("ALL processes completed")

    
        
