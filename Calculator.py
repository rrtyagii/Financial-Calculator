import math as m

"""
Listing the functions required to perform the basic calculations in a financial calculator


PV - Present Value
FV - Future Value
i - interest rate( the nominal annual rate)
n - number of compounding periods in the term 
PMT - periodic payment
m - compounding frequency (compounding internvals)
Y - number of years in term

"""

class CalculatorState:
    #basic operations
    def add(self, value1,value2):
        return value1+value2

    def subtract(self, value1, value2):
        return value1-value2

    def multiply(self, value1,value2):
        return value1*value2

    def divide(self, value1,value2):
        if isinstance(value2,int) and isinstance(value1,int):
            return value1//value2
        else:
            return value1/value2

    def power(self, value1,value2):
        return m.pow(value1,value2)

    #basic operations to find compound and simple interest and effective annual rate
    def simple_Interest(self,principle,time,rate):
        assert (time>0), "Time cannot be Negative!"
        assert rate>0, "interest rate cannot be Negative!"

        return principle*time*(rate/100)

    def compound_Interest(self, principle, time, rate,freq_compounding):
        assert (time>0), "Time cannot be Negative!"
        assert rate>0, "interest rate cannot be Negative!"
        assert freq_compounding>0, "Frequency of Compounding, n,  cannot be Negative!"
        app_rate = rate/100

        return principle * m.pow( 1 + (app_rate/time),time*freq_compounding )

    def effective_Annual_Rate(self,i,n):
#        assert (time>0), "Time cannot be Negative!"
        assert i>0, "interest rate cannot be Negative!"
        assert n>0, "number of compounding periods in the term, n,  cannot be Negative!"
        # i=i/100
        i_eff = m.pow(1+i,n) - 1
        return i_eff

    def i_continous_comp(self,i):
        assert i>0, "interest rate cannot be Negative!"
        # i=i/100
        i_max = m.pow(m.e,i) -1
        return i_max

    #For single Sum calculations

        """
        PV - Present Value
        FV - Future Value
        i - interest rate( the nominal annual rate)
        n - number of compounding periods in the term 
        PMT - periodic payment
        m - compounding frequency (compounding internvals)
        Y - number of years in term
       """


    def future_val(self, PV, i, n):
        assert i>0, "Interest rate cannot be negative"
        assert n>0 , "Number of compounding periods in the term cannot be negative"
        # i=i/100
        FV= PV* m.pow(1+i,n)
        return FV


    def present_val(self, FV, i, n):
        assert i>0, "Interest rate cannot be negative"
        assert n>0 , "Number of compounding periods in the term cannot be negative"
        # i=i/100
        PV = FV/(m.pow(1+i, n))
        return PV

    def num_of_period(self,FV,PV,i):
        assert i>0, "Interest rate cannot be negative"
        # i=i/100
        n = (m.log(FV/PV,m.e)) / (m.log(1+i))
        return n

    def interest_rate(self,FV,PV,n):
        assert n>0, "Number of compounding periods in the term cannot be negative"

        i=m.pow(FV/PV,1/n) -1
        return i

        #For Annuity calculations

        """
        PV - Present Value
        FV - Future Value
        i - interest rate( the nominal annual rate)
        n - number of compounding periods in the term 
        PMT - periodic payment
        m - compounding frequency (compounding internvals)
        Y - number of years in term
       """

    def present_value_ord(self,i,n, PMT):
        #finding present value of ordinary annuity
#        assert i is not 0, "Error: Cannot divide by 0"
        assert i>0, "Interest rate cannot be negative"
        assert n>0 , "Number of compounding periods in the term cannot be negative"

        PV = PMT*( ( 1 - m.pow(1+i,-n))/ i )
        return PV

    def number_periods(self, PV,i, PMT):
        #finding the number of periods ,n, -present value of annuity
        assert i>0, "Interest rate cannot be negative"

        n = - ( m.log( 1- ( (i*PV)/PMT) ) ) / (m.log(1+i))
        return n

    def payment_per_period(self, i,n,PV):
        #finding payment, PMT- PV of annuity
        assert i>0, "Interest rate cannot be negative"
        PMT = (i*PV)/(1 - ( m.pow (1+i), -n))
        return PMT


    def future_value_ord(self,PMT, i,n):
        #finding future value of ordinary annuity
        assert i>0, "Interest rate cannot be negative"
        assert n>0 , "Number of compounding periods in the term cannot be negative"

        FV= PMT* ( (m.pow( 1+i , n)-1 )/i )
        return FV

    def number_periods_FV(self, FV,i, PMT):
        #finding the number of periods ,n, -future value of annuity
        assert i>0, "Interest rate cannot be negative"
#        assert n>0 , "Number of compounding periods in the term cannot be negative"

        n= m.log( (i*FV)/(PMT) +1)/m.log(1+i)
        return n

    def payment_per_period_FV(self, i,n,FV):
        #finding payment, PMT- FV of annuity
        assert i>0, "Interest rate cannot be negative"
        assert n>0 , "Number of compounding periods in the term cannot be negative"

        PMT = (i*FV) / (m.pow(1+i,n) -1)
        return PMT


    #Annuity DUE
    def perpetuity(self, PMT, i):
        #PV of annuity
        PV = PMT/i
        return PV