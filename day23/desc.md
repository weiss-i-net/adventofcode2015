



Day 23 - Advent of Code 2015



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2015/about)
* [[Events]](/2015/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Settings]](/2015/settings)
* [[Log Out]](/2015/auth/logout)
weiss-i-net 11\*#       /\*[2015](/2015)\*/

* [[Calendar]](/2015)
* [[AoC++]](/2015/support)
* [[Sponsors]](/2015/sponsors)
* [[Leaderboard]](/2015/leaderboard)
* [[Stats]](/2015/stats)




## --- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.


The manual explains that the computer supports two [registers](https://en.wikipedia.org/wiki/Processor_register) and six [instructions](https://en.wikipedia.org/wiki/Instruction_set) (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named `a` and `b`, can hold any [non-negative integer](https://en.wikipedia.org/wiki/Natural_number), and begin with a value of `0`. The instructions are as follows:


* `hlf r` sets register `r` to *half* its current value, then continues with the next instruction.
* `tpl r` sets register `r` to *triple* its current value, then continues with the next instruction.
* `inc r` *increments* register `r`, adding `1` to it, then continues with the next instruction.
* `jmp offset` is a *jump*; it continues with the instruction `offset` away *relative to itself*.
* `jie r, offset` is like `jmp`, but only jumps if register `r` is *even* ("jump if even").
* `jio r, offset` is like `jmp`, but only jumps if register `r` is `1` ("jump if *one*", not odd).


All three jump instructions work with an *offset* relative to that instruction. The offset is always written with a prefix `+` or `-` to indicate the direction of the jump (forward or backward, respectively). For example, `jmp +1` would simply continue with the next instruction, while `jmp +0` would continuously jump back to itself forever.


The program exits when it tries to run an instruction beyond the ones defined.


For example, this program sets `a` to `2`, because the `jio` instruction causes it to skip the `tpl` instruction:



```
inc a
jio a, +2
tpl a
inc a

```

What is *the value in register `b`* when the program in your puzzle input is finished executing?



To begin, [get your puzzle input](23/input).


Answer:  


You can also [Shareon
 [Twitter](https://twitter.com/intent/tweet?text=%22Opening+the+Turing+Lock%22+%2D+Day+23+%2D+Advent+of+Code+2015&url=https%3A%2F%2Fadventofcode%2Ecom%2F2015%2Fday%2F23&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void(0);)] this puzzle.





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



