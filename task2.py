#FOCP FINAL TASK 2
runner, time= [], [] 
def avg(time):
    '''Calculates Average in Minutes and Seconds'''
    average=sum(time)/len(time)
    m_avg, s_avg= divmod(average, 60) #converting average in minutes and seconds format 
    print(f'Average Time: {int(m_avg)} {"minute" if m_avg<=1 else "minutes"}, {int(s_avg)} {"second" if s_avg<=1 else "seconds"}')
def minimum(time): 
    '''Determines minimum time in Minutes and Seconds'''
    minimum=min(time) 
    m_min, s_min= divmod(minimum, 60) 
    print(f'Fastest Time: {int(m_min)} {"minute" if m_min<=1 else "minutes"}, {int(s_min)} {"second" if s_min<=1 else "seconds"}')
def maximum(time):
    '''Determines maxumum time in Minutes and Seconds'''
    maximum=max(time) 
    m_max, s_max= divmod(maximum, 60) 
    print(f'Slowest Time: {int(m_max)} {"minute" if m_max<=1 else "minutes"}, {int(s_max)} {"second" if s_max<=1 else "seconds"}')
def winner(time, runner):
    '''Determines Winner'''
    index=time.index(min(time)) 
    print(f'\nBest Time Here: Runner #{runner[index]}')
def main():
    print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!")
    while True: 
        entry=input("> ")
        if entry =="END": 
            if len(runner)==0: 
                print("No data found. Nothing to do. What a pity.") 
            else: 
                print("Total Number:", len(runner), "\n") 
                avg(time) 
                minimum(time) 
                maximum(time) 
                winner(time,runner)
            break 
        split_entry=entry.split("::") 
        try: 
            int(split_entry[0]) 
            int(split_entry[1]) 
            i = int(split_entry[0])
            if i in runner:
                print("Runner is already registered! Ignorning. Carry on.")
            else:
                runner.append(int(split_entry[0])) 
                time.append(int(split_entry[1])) 
        except: 
            print("Error in data stream. Ignorning. Carry on.")
if __name__ == '__main__':
  main()