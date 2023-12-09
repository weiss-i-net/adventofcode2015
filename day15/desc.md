



Day 15 - Advent of Code 2015



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2015/about)
* [[Events]](/2015/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Settings]](/2015/settings)
* [[Log Out]](/2015/auth/logout)
weiss-i-net 11\*#    var y=[2015](/2015);

* [[Calendar]](/2015)
* [[AoC++]](/2015/support)
* [[Sponsors]](/2015/sponsors)
* [[Leaderboard]](/2015/leaderboard)
* [[Stats]](/2015/stats)




## --- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.


Your recipe leaves room for exactly `100` teaspoons of ingredients. You make a list of the *remaining ingredients you could use to finish the recipe* (your puzzle input) and their *properties per teaspoon*:


* `capacity` (how well it helps the cookie absorb milk)
* `durability` (how well it keeps the cookie intact when full of milk)
* `flavor` (how tasty it makes the cookie)
* `texture` (how it improves the feel of the cookie)
* `calories` (how many calories it adds to the cookie)


You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The *total score* of a cookie can be found by adding up each of the properties (negative totals become `0`) and then multiplying together everything except calories.


For instance, suppose you have these two ingredients:



```
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

```

Then, choosing to use `44` teaspoons of butterscotch and `56` teaspoons of cinnamon (because the amounts of each ingredient must add up to `100`) would result in a cookie with the following properties:


* A `capacity` of `44*-1 + 56*2 = 68`
* A `durability` of `44*-2 + 56*3 = 80`
* A `flavor` of `44*6 + 56*-2 = 152`
* A `texture` of `44*3 + 56*-1 = 76`


Multiplying these together (`68 * 80 * 152 * 76`, ignoring `calories` for now) results in a total score of `62842880`, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.


Given the ingredients in your kitchen and their properties, what is the *total score* of the highest-scoring cookie you can make?



To begin, [get your puzzle input](15/input).


Answer:  


You can also [Shareon
 [Twitter](https://twitter.com/intent/tweet?text=%22Science+for+Hungry+People%22+%2D+Day+15+%2D+Advent+of+Code+2015&url=https%3A%2F%2Fadventofcode%2Ecom%2F2015%2Fday%2F15&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void(0);)] this puzzle.





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



