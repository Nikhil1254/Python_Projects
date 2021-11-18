#include<stdio.h>
#include<stdlib.h>


#define ESC 0
#define UP 1
#define DOWN 2
#define LEFT 3
#define RIGHT 4


int size;


int SetLevel();
void SetMatrix(int A[][size+1]);
void ShowMatrix(int A[][size+1]);
int ReadKey();
int CheckWin(int A[][size+1]);
int ShiftUP(int A[][size+1]);
int ShiftDOWN(int A[][size+1]);
int ShiftLEFT(int A[][size+1]);
int ShiftRIGHT(int A[][size+1]);


int main()
{
	int move=500;
	
	size = SetLevel();
	system("cls");
	
	int A[size+1][size+1];

	SetMatrix(A);
	while(move)
	{
		printf("\nMoves Remaining : %d",move);
		ShowMatrix(A);

		if(CheckWin(A))
		{
			printf("\nCongratulation you win in %d moves", 500-move);
			printf("\nPress any key to exit.....");
			getch();
			exit(0);
		}

		switch(ReadKey())
		{
			case ESC :	exit(0);

			case UP : if(!ShiftUP(A))
					  move++;
					  break;

			case DOWN : if(!ShiftDOWN(A))
					    move++;
						break;

			case LEFT : if(!ShiftLEFT(A))
						move++;
						break;

			case RIGHT : if(!ShiftRIGHT(A))
						 move++;
						 break;

			default : move++;
		}

		system("cls");
		move--;
	}

	getch();
	
	return 0;
}


int SetLevel()
{
	int level;
	int check = 1;
	
	do
	{
		printf("Press 1 for 2*2 \n");
		printf("Press 2 for 3*3 \n");
		printf("Press 3 for 4*4 \n");
		printf("Enter level : ");
		scanf("%d",&level);
		
		if (level>0 && level<4)
			check = 0;
		else
			printf("Enter Valid level !!!\n");
	}while(check);
	
	return level;	
}


void SetMatrix(int A[][size+1])
{
	int pool[(size+1)*(size+1)-1];
	int maxIndex , index,i,j;
	
	maxIndex = (size+1)*(size+1)-2;
	
	for(i=1 ; i<(size+1)*(size+1) ; i++)
	{
		pool[i-1] = i;
	}

	srand(time(NULL));
	for (i=0 ; i<=size ; i++)
	{
		for (j=0 ; j<=size ; j++)
		{
			if(maxIndex>=0)
			{
				index = rand()%(maxIndex+1);
				A[i][j] = pool[index];
				pool[index] = pool[maxIndex];
				maxIndex--;
			}

			else
			{
				A[i][j]=0;
			}
		}
	}
}


void ShowMatrix(int A[][size+1])
{
	int i,j;

	printf("\n-------------------------\n|");
	for (i=0 ; i<=size ; i++)
	{
		for (j=0 ; j<=size ; j++)
		{
			if(A[i][j] != 0)
				printf(" %-2d | ",A[i][j]);												// - means right aligned and 2 means minimum 2 space ghenar ek no display karayala

			else
				printf("    | ");
		}
		printf("\n-------------------------\n");
		if(i!=size)
			printf("|");
	}	
}


int ReadKey()
{
	int ch;
	ch = getch();

	if(ch==224)										// Scan code (UP arrow press kele tar input buffer madhe 2 no yetat 224,72)
		ch = getch();								// Ithe getch input buffer madun value ghenar

	switch(ch)
	{
		case 27 : 
			return(ESC);
		case 72 :
			return(UP);
		case 80 :
			return(DOWN);
		case 75 :
			return(LEFT);
		case 77 :
			return(RIGHT);

		default:
			return(9);
	}
}


int CheckWin(int A[][size+1])
{
	int i,j,k=0;

	for(i=0 ; i<=size ; i++)
	{
		for(j=0 ; j<=size ; j++)
		{
			k<((size+1)*(size+1)-1) ? k++ : (k=0);
			if (A[i][j]!=k)
				return 0;
		}
	}
	return 1;
}


int ShiftUP(int A[][size+1])
{
	int i,j,temp,zeroFound=0;

	for(i=0 ; i<=size ; i++)
	{
		for(j=0 ; j<=size ; j++)
		{
			if(A[i][j] == 0)
			{
				zeroFound = 1;
				break;
			}
		}
		if(zeroFound == 1)
			break;
	}

	if(i==0)
		return 0;														// Shifting not possible
	else
	{
		temp = A[i][j];
		A[i][j] = A[i-1][j];
		A[i-1][j] = temp;

		return 1;
	}
}


int ShiftDOWN(int A[][size+1])
{
	int i,j,temp,zeroFound=0;

	for(i=0 ; i<=size ; i++)
	{
		for(j=0 ; j<=size ; j++)
		{
			if(A[i][j] == 0)
			{
				zeroFound = 1;
				break;
			}
		}
		if(zeroFound == 1)
			break;
	}

	if(i==size)
		return 0;														// Shifting not possible
	else
	{
		temp = A[i][j];
		A[i][j] = A[i+1][j];
		A[i+1][j] = temp;

		return 1;
	}
}


int ShiftLEFT(int A[][size+1])
{
	int i,j,temp,zeroFound=0;

	for(i=0 ; i<=size ; i++)
	{
		for(j=0 ; j<=size ; j++)
		{
			if(A[i][j] == 0)
			{
				zeroFound = 1;
				break;
			}
		}
		if(zeroFound == 1)
			break;
	}

	if(j==0)
		return 0;														// Shifting not possible
	else
	{
		temp = A[i][j];
		A[i][j] = A[i][j-1];
		A[i][j-1] = temp;

		return 1;
	}
}


int ShiftRIGHT(int A[][size+1])
{
	int i,j,temp,zeroFound=0;

	for(i=0 ; i<=size ; i++)
	{
		for(j=0 ; j<=size ; j++)
		{
			if(A[i][j] == 0)
			{
				zeroFound = 1;
				break;
			}
		}
		if(zeroFound == 1)
			break;
	}

	if(j==size)
		return 0;														// Shifting not possible
	else
	{
		temp = A[i][j];
		A[i][j] = A[i][j+1];
		A[i][j+1] = temp;

		return 1;
	}
}
