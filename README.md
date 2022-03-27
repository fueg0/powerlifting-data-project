# Powerlifting Data Science Final FALL2021

Objective:
This project was created with the aim of collecting the totals of powerlifters across drug-tested competitive federations in order to observe if there is any observable difference in the composition of a lifter's total as they become more skilled. In this scenario, I split totals into sections by the how they fell into a standard deviation range of all totals and considered the mean an "average-skilled lifter" for that weight class or category. Standard deviations to the right (aka those with higher than average totals) represented higher-skilled lifters, and vice versa for the left.

After splitting totals into these ranges, I could calculate what percentage of their total was comprised of their squats, bench presses, and deadlifts on average for that "skill range" in order to see if these average compositions changed between 

Data:
I used two main datasets to check if my results would look similar, one being all recorded USA Powerlifting meets, since that is the federation that I compete in, and the other being all recorded International Powerlifting Federation meets, which contain the USAPL meets as a subset within them.

I compared this data between raw lifters in each weight class for men, for women, and also cumulatively between all men or all women. I did the same for equipped lifters, which (expectedly) displayed a slightly different composition of totals but still yielded differences in the compositions between skill ranges.

Any lifters who are unable to complete at least one lift in each of the disciplines (squat, bench press, and deadlift) do not post an accumulated total, so those data points were cleaned out of the data set since they would drive down averages- which not representative of lifters who completed a full competition. Similarly, anyone else who was disqualified for any other reason (rule-breaking, failure/refusal to report to doping control, etc) were also removed. For the sake of performing a data analysis on lifters assumde to be competing without the use of performance-enhancing or otherwise banned drugs, I made the choice to remove those data points, since I sought out datasets from drug-tested federations for that reason.

Results:
The results of this show that as skill/strength increases, the percentage of a total comprised by the squat tends to rise and equal or surpass that of the deadlift. In the upper-range weight classes, this progression begins sooner and tends to exceed the squats further than in other classes. For lighter weight classes, the squats also rise, but rarely reach or exceed the deadlifts. When it came to the bench press, it was interesting to note that it stayed between 20-25% of a lifter's total, with a very small amount of occurrences outside of that range, and seemlingly little pattern as to whether it was closer to 20% or 25%.
