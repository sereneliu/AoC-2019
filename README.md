# Learning Log

Okay, so I haven't coded in Python in a reeeeeeally long time, so I did go back to AoC-2018 briefly in November to freshen up. I didn't end up doing much, but it helped to remind me that Java is really that much more verbose. 

Anyway, I hope to get through as many puzzles as possible and my goal is to learn something new with each one, especially from the part 2 solutions that tend to be less brute forceable.

## Day 1

I was on the road, so on one hand, I had plenty of free time on my hands, but on the other hand, I also had unreliable internet and an urge to complete asap in order to avoid motion sickness. 

I ended up writing the code for part 1 on my phone during lunch and ran it in the car on my laptop afterwards. I used to have to write a lot of print statements because I couldn't visualize very well what was happening without doing so, so getting it right on the first try without a way to test what I wrote felt really good, even if part 1 was super easy.

When we were visiting a temple earlier in the day, some of my relatives were discussing this neverending story that they were told as kids. My husband called it recursive storytelling and I replied, "Gah, I don't even remember how to write recursive functions anymore!" Well, speak of the devil. I went the looping route, but I will come back to this.

Also, really happy that I decided to separate out the fuel calculation in part 1 so that I didn't have to refactor anything in part 2.

Heh, forgot to add the very first lesson I learned: `//` gives me exactly what I need, rounding down to the nearest whole number without the remainder.

## Day 2

Didn't have time to work on this puzzle day of, so will come back to it when I have time. In general, my goal is to finish each day before that day is over. If I don't, I move on.

## Day 3

This one took me awhile longer to solve, mostly due to stupid mistakes. My original solution for part 1 was fast enough, but when I changed stuff for part 2, then it slowed considerably. I will definitely need to come back to this one with a faster solution time.

## Day 4

For this puzzle, I struggled a lot with how to structure my code properly. It took a long time because I ended up refactoring over and over again. I'm happier with where it is now, but I'm sure there's room for improvement.

Well, just looked at the solution thread on Reddit: https://www.reddit.com/r/adventofcode/comments/e5u5fv/2019_day_4_solutions/

As it turns out, I'm not thinking about these puzzles in the right way. My biggest mistake is not taking advantage of built-in functions and I'm basically rewriting a version of it. Sometimes, it's because I'm not aware of what's out there. Clever solutions I've seen in Python include:
* checking if the sorted password is the same as the original password for the no-decrease requirement
* checking `2 in map(n.count, n)` - haven't quite figured out why it works but I get the idea of it
* `sum(function(n) for n in range)` instead of assigning a variable and increasing it on every iteration in the range
