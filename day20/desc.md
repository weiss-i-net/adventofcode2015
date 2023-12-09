



Day 20 - Advent of Code 2015



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2015/about)
* [[Events]](/2015/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Settings]](/2015/settings)
* [[Log Out]](/2015/auth/logout)
weiss-i-net 11\*#         //[2015](/2015)

* [[Calendar]](/2015)
* [[AoC++]](/2015/support)
* [[Sponsors]](/2015/sponsors)
* [[Leaderboard]](/2015/leaderboard)
* [[Stats]](/2015/stats)




## --- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: `1`, `2`, `3`, `4`, `5`, and so on.


Each Elf is assigned a number, too, and delivers presents to houses based on that number:


* The first Elf (number `1`) delivers presents to every house: `1`, `2`, `3`, `4`, `5`, ....
* The second Elf (number `2`) delivers presents to every second house: `2`, `4`, `6`, `8`, `10`, ....
* Elf number `3` delivers presents to every third house: `3`, `6`, `9`, `12`, `15`, ....


There are infinitely many Elves, numbered starting with `1`. Each Elf delivers presents equal to *ten times* his or her number at each house.


So, the first nine houses on the street end up like this:



```
House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.

```

The first house gets `10` presents: it is visited only by Elf `1`, which delivers `1 * 10 = 10` presents. The fourth house gets `70` presents, because it is visited by Elves `1`, `2`, and `4`, for a total of `10 + 20 + 40 = 70` presents.


What is the *lowest house number* of the house to get at least as many presents as the number in your puzzle input?



Your puzzle input is `33100000`.


Answer:  


You can also [Shareon
 [Twitter](https://twitter.com/intent/tweet?text=%22Infinite+Elves+and+Infinite+Houses%22+%2D+Day+20+%2D+Advent+of+Code+2015&url=https%3A%2F%2Fadventofcode%2Ecom%2F2015%2Fday%2F20&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void(0);)] this puzzle.





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



