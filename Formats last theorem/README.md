# Formats last theorem

Formatstring bug in the **vuln()** function

```c
void __noreturn vuln()
{
  char format[104]; // [rsp+0h] [rbp-70h] BYREF
  unsigned __int64 v1; // [rsp+68h] [rbp-8h]

  v1 = __readfsqword(0x28u);
  while ( 1 )
  {
    puts("I won't ask you, what your name is. It's getting kinda old at this point");
    __isoc99_scanf("%100s", format);
    puts("you entered");
    printf(format);       //format string here
    puts(&byte_8B3);
    puts(&byte_8B3);
  }
}
```
Program compiled on **ubuntu:18.04** that mean libc version is 2.27

I solved this with overwrite **__free_hook** to **one_gadget**


[Full Sript](https://github.com/L29/Binary-Writeup/blob/main/dCTF/Formats%20last%20theorem/exploit.py)

![Flag](format.png)
