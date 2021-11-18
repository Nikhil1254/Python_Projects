import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split  # data spliting sathi test ani train data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score # r2 chi value sathi performance check

-
def welcome():
    print("\nWelcome To Salary Prediction System  ")
    print("Press Enter Key To Proceed  ")
    input()

def checkcsv():     # currect directory madhe jithe apla program ahe tithe jivdhe csv file ahet te return kartay
    csv_files = []
    cur_dir = os.getcwd() # current directory det
    content_list = os.listdir(cur_dir) # sagle folders ani files tya directory madhli milavli
    for x in content_list:
        if x.split('.')[-1] == 'csv':
            csv_files.append(x)
    if len(csv_files) == 0:
        return 'No csv file in the directory.'  # ethech project end karva lagel jar csv file ch nasel tr
    else:
        return csv_files

def display_and_select_csv(csv_files):
    i=0
    for file_name in csv_files:
        print(i,'...',file_name)
        i+=1
    return csv_files[int(input('Select file to create machine learning model  '))]

def graph(X_train,Y_train,regressionObject,X_test,Y_test,Y_pred):
    plt.scatter(X_train,Y_train,color='red',label='training data')  # sagla data plot hoil
    plt.plot(X_train,regressionObject.predict(X_train),color="blue",label="Best fit") # training data var predict kartoy mhanje regression line ch banun janar
    plt.scatter(X_test,Y_test,color="green",label="test data")
    plt.scatter(X_test,Y_pred,color="black",label="predicted test data")
    plt.title("Salary vs Experience")
    plt.xlabel("Years of experience")
    plt.ylabel("Salary")
    plt.legend() ## to show labels we require legend function
    plt.show()

def main():
    welcome()
    try:
        csv_files = checkcsv()
        if csv_files == 'No csv file in the directory.':
            raise FileNotFoundError()
        csv_file = display_and_select_csv(csv_files)
        print(csv_file,"is selected ")
        print("Reading CSV file ")
        print("Creting Dataset ")
        dataset = pd.read_csv(csv_file)
        print("Dataset created. ")
        X = dataset.iloc[:,:-1].values  # purn experience vala column X madhe yeil
        '''
            strat_value : end_value
            end_value is excluded 
            so for columns i have given :-1,
            and we only have 2 columns
            start_value = 0;
            end_value = -1;
            mhanje last column exclude hoil fakt 0 vala include hoil as we have only two columns
            
            
            // iloc stands for index location.
        
        '''
        Y = dataset.iloc[:,-1].values # salary vala purn column yat yeil
        s = float(input("Enter test Data size (between 0 and 1)  "))
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=s) # this function returns 4 values,x cha tarin-test,y cha train-test ashe 4 calues return karto
        print("Module creation in progress...")
        regressionObject = LinearRegression() # LinearRegression class cha object banavla
        '''
            regression line kadhu ata apan
        '''
        regressionObject.fit(X_train,Y_train) #best fit regression line create karnar
        print("Module is created.  ")
        print("Press ENTER key to predict test data in trained model  ")
        input()

        Y_pred = regressionObject.predict(X_test)
        i = 0
        print('X_test', '...', 'Y_test', '...','Y_pred')
        while i<len(X_test):
            print(X_test[i],'...',Y_test[i],'...',Y_pred[i])
            i+=1
        print("Press ENTER key to see above result in graphical format  ")
        input()
        graph(X_train,Y_train,regressionObject,X_test,Y_test,Y_pred)

        r2 = r2_score(Y_test,Y_pred)
        print("Our model is %2.2f%% accurate"%(r2*100))

        print("Now you can predict salary of an employee using our model.  ")
        print("\nEnter experince in years of candidate,seperated by comma  ")

        try:
            exp = [float(e) for e in input().split(',')] # list of float values of experiences
            ex = []
        except :
            print("You haven't entered any values,Press ENTER to EXIT.",end=" ")
            input()
            return
        
        for x in exp:
            ex.append([x]) # list item append kartoy
        experience = np.array(ex)
        salaries = regressionObject.predict(experience)

        plt.scatter(experience,salaries,color="orange")  #experience
        plt.xlabel("Experience  ")
        plt.ylabel("Salaries  ")
        plt.show()

        d = pd.DataFrame({'Experience ':exp,"Salaries ":salaries})
        print(d)
        print("Press Enter to EXIT.")
        input()

    except FileNotFoundError:
        print("No CSV file in the directory.  ")
        print("Press ENTER key to exit.  ")


if __name__ == "__main__":
    main()
