



Day 12 - Advent of Code 2015



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2015/about)
* [[Events]](/2015/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Settings]](/2015/settings)
* [[Log Out]](/2015/auth/logout)
weiss-i-net 11\*#    <y>[2015](/2015)</y>

* [[Calendar]](/2015)
* [[AoC++]](/2015/support)
* [[Sponsors]](/2015/sponsors)
* [[Leaderboard]](/2015/leaderboard)
* [[Stats]](/2015/stats)




## --- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.


They have a [JSON](http://json.org/) document which contains a variety of things: arrays (`[1,2,3]`), objects (`{"a":1, "b":2}`), numbers, and strings. Your first job is to simply find all of the *numbers* throughout the document and add them together.


For example:


* `[1,2,3]` and `{"a":2,"b":4}` both have a sum of `6`.
* `[[[3]]]` and `{"a":{"b":4},"c":-1}` both have a sum of `3`.
* `{"a":[-1,1]}` and `[-1,{"a":1}]` both have a sum of `0`.
* `[]` and `{}` both have a sum of `0`.


You will not encounter any strings containing numbers.


What is the *sum of all numbers* in the document?



To begin, [get your puzzle input](12/input).


Answer:  


You can also [Shareon
 [Twitter](https://twitter.com/intent/tweet?text=%22JSAbacusFramework%2Eio%22+%2D+Day+12+%2D+Advent+of+Code+2015&url=https%3A%2F%2Fadventofcode%2Ecom%2F2015%2Fday%2F12&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void(0);)] this puzzle.





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



