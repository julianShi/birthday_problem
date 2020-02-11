# Problem
There are M members in a group. The birthday of a member is uniformly random in a year. The group celebrates if there is at least one member who is on birthday at a day. Then, how many days in average does the group celebrate in a year? 

# Solution
## Probability analysis
The average day can be calculated by 
```
\sum_{k=1}^{N} k p(k)
```
where `N` is the number of days in a year, `p(k)` is the probability that `k` exact days are birthdays in a year. 

Probability is calculated by the permutation when there are `k` exact days, divided by the all posibilities when M members random choose among N days. 
```
p(k) = permutation / (N**M)
```

## Dynamic programming
The problem is solved using dynamic programming. Let `f(n,k)` denotes the permutation when there are M member in the group, n days in a year, and exact k days are birthdays. Let `bi(a,b)` denotes the binominal coefficient choosing b in a.
```
f(1,1)=bi(1,1)*(1**M)
f(2,1)=bi(2,1)*f(1,1), f(2,2)=(2**M)-f(2,1)
f(3,1)=bi(3,1)*f(1,1), f(3,2)=bi(3,2)*f(2,2), f(3,3)=(2**M)-f(3,1)-f(3,2)
f(n,k)=bi(n,k)*f(k,k) if k<n
```
# Examples
## Example 1
When there are 365 members in a group, and 365 days in a year, the `average_birthdays(365,365)` returns
```
average_days=39841418807732193848566864788709139859965527162458859745336255193442127578223196549507317164549054214350446758172050372468971662980572190991509770644668355527861667706656850068622649736185388960670447061394911116921900408401185319946542598181970571987439078231077356957079537414571018187750629637704565638684356192912780263566726213697164324396200544738228822937527808720219704166364624033102427482086326457978324329608013172159353289836335221514841501306224599231908727421955574618450497620467621338774188918734078947808343738910927976193061229161425424769489884473039373175451368703962755625233693932007438566445339081270930941744848490560916955227312166032982239933800023074535803360812781570807016868892095497582810196284221395752013218506846408397736740457086827824588274073793411243517986040081601926736302828264775603335718475952190652832394612091832255332626301723954665959779826835607325114991234902509027950778814544198763283865
```
The 
```
average_days/(365**365)
```
returns 230.91 days on https://www.dcode.fr/big-numbers-division

## Example 2
When there are 500 members in a group, and 365 days in a year, the average number of birthdays is 272.41

## Example 3
When there are 1000 members in the group, the probabilities when there are 365 birthdays is as low as 1.7123209303595205e-12
