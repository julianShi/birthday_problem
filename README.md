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
When there are 365 members in a group, and 365 days in a year, the `average_birthdays(365,365)` returns `230.91`. 

The probabilities of k birthdays are distributed like

![birthday probabilities](birthday_probabilities.jpg)

## Example 2
When there are 500 members in a group, and 365 days in a year, the average number of birthdays is `272.41`.

## Example 3
When there are 1000 members in the group, the probabilities when there are 365 birthdays is as low as `1.7123209e-12`
