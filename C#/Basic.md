

```c#
char.IsLetter(p, 3)
```

> `isletter(x,inde)``是否为字母`

```c#
char.IsNumber(p, 3)
```

> `isnumber(x,inde)``是否为数字类型`

```c#
char.IsLower(p, 3)
```

> `islower(p,index)``是否为小写字母`

```c#
char.IsPunctuation(p, 3)
```

> `ispunctuation(p,index)``是否为标点符号`

```c#
char.IsLetterOrDigit(p, 3)
```

> `IsLetterOrDigit(p,index)``是否为字母或十进制数字`
>
> 小数点后留后两位(四舍五入)

```c#
double b=2.5444;
string c=b.toString("0.00");
convert.Toint32(c);
```

### String常用方法

```c#
String str = String.Empty
```

> `Equals()` ：**比较两个字符串的值是否相等**
>
> `ToLower()`：**将字符串转换成小写形式**
>
> `IndexOf()`：**查找某个字符在字符串中的位置**
>
> `SubString()`：**从字符串中截取子字符串**
>
> `Join()`：**连接字符串**
>
> `Split()`：**分割字符串**
>
> `Trim()`：**去掉字符串两边的空格**
>
> `Distinct()`：**删除重复值**

### 输出方法

> `數組輸出`

```c#
static void PR(int[] nums)
   {
       foreach (int i in nums)
       {
           Console.Write(i + " ");
       }
       Console.WriteLine();
   }
```

> `普通輸出`

```c#
static void prl(int n)
     {
         Console.WriteLine(n);
     }
```

> `一維數組輸出`

```c#
static void pr2l(int[][] nums7)
     {
         for(int i = 0; i < nums7.Length; i++)
         {
             for(int j = 0; j < nums7[0].Length; j++)
             {
                 Console.Write(nums7[i][j] + " ");
             }
             Console.WriteLine();
```

> `char[]``遍历输出`

```c#
static void prc(char[] c)
     {
         foreach(char h in c)
         {
             Console.Write(h + " ");
         }
     }
```

### 二分查找

> 输入：`nums=[-1,0,3,5,9,12]` `target=9`
>
> 输出：`4`
>
> 解释：`9``出现在``numsongoing``并且下标位``4`

```c#
static int Search(int[] nums,int target){
	for(int i =0;i<nums.Length;i++){
		if(nums[i]==target){
			return i;
		}
	}
	return -1;
}
```

### System.IO空间 Directory方法

> `DirectoryInfo dinfo = new DirectoryInfo("`文件路径`");`
>
> 文件创建时间

```c#
Console.WriteLine("创建时间" + dinfo.CreationTime.ToLongTimeString());
```

> 文件最近访问时间

```c#
Console.WriteLine("最近访问时间 " + dinfo.LastAccessTime.ToLongDateString());
```

> 上级文件夹

```c#
Console.WriteLine("上级文件架" + dinfo.Parent.Name);
```

> 有子文件夹

```c#
Console.WriteLine("有子文件夹" + dinfo.GetDirectories().Length.ToString());
```

> 包换文件

```c#
Console.WriteLine("包含文件" + dinfo.GetFiles().Length.ToString());
```

> 遍历路径下的文件名&输出出来

```c#
FileInfo[] fs = dinfo.GetFiles();
         foreach (FileInfo f in fs)
         {
             Console.WriteLine(f.Name);
         }
```

### LINQ

> 替换字符

```c#
string s="a b c d";
string.Join("",s.Select(c ==> c ==' ' ? "%20" : c + ""));
```
### 字典

> 字典的Add

```c#
Dictionary<string, int> cache = new Dictionary<string, int>();
cache["1"] = 1;
cache.Add("2" , 2);
```
### 正则表达式

> 正则表达式

```c#
//eg: a.b a和b之间只有一个字符
//符合：axb , acb , aab , a?b


//[] 字符组：表示在字符组中罗列出来的字符任意取单个字符
//eg: a[xyz]b
//符合：axb , ayb , azb
//
//eg: a[a-bA-Z0-9]b
//a~z,A~Z,0~9都可以


// | 表示或，优先级最低
// () 表示改变优先级 
//eg: a(x|y)b a b之间要么是x，要么是y
//eg: z|food 要么匹配z ，要么匹配food


//* 表示限制表达式前面出现0次或多次
//eg: a.*b
//符合：ab , axb , axxxxb
//
//eg: a.+b
//符合：axb , axxxxb
//不符合：ab


// ? 表示字符出现0次或0次
//eg: a.?b
//符合：axb , ab
//不符合：axxxxxxb


//eg: {n} 限定出现次数，表示字符必须出现n次
//[0-9]{3}
//符合：123
//
//eg: {n,} 表示最少出现n次
//
//eg: {n,m} 表示最少出现n次，最多出现m次


//eg: a[^xyz]b 表示a和b之间不能出现xyz任意字符
//符合：aab ， abb
```

```c#
Console.Write("PLZ Select Case:");
string selectcase = Console.ReadLine();
switch (selectcase)
{
	case "a":
		Console.Write("Enter Phone Number");
		string num = Console.ReadLine();
        	//电话号验证
		bool b = System.Text.RegularExpressions.Regex.IsMatch(num, @"^\d[0-9]{10}$");
		Console.WriteLine(b);
		break;
	case "b":
		Console.Write("Enter Post Number:");
		string num1 = Console.ReadLine();
        	//邮政代码验证
		bool b1 = System.Text.RegularExpressions.Regex.IsMatch(num1, "^[0-9]{6}$");
		Console.WriteLine(b1);
        break;
    case "c":
        Console.Write("Enter Name:");
        string num2 = Console.ReadLine();
        //开头jin的名字验证
        bool b2 = System.Text.RegularExpressions.Regex.IsMatch(num2, "^jin$");
        Console.WriteLine(b2);
        break;
    case "d":
		string email = "sgfs@qq.com jkjlsf 你好 wsf@vip.com.cn 5121s2dfg jxct@126.com *())999 sgfs#163.com sdfa@163.com sdfgs@qq.com";
        	//邮件验证并提取
		System.Text.RegularExpressions.MatchCollection coll1 = System.Text.RegularExpressions.Regex.Matches(email, @"([-a-zA-Z_0-9.]+)@([a-zA-Z0-9]+(\.[A-Za-z]+)+)");
		foreach(System.Text.RegularExpressions.Match item in coll1)
		{
            Console.WriteLine(item.Value);
        }
        Console.WriteLine();
        foreach (System.Text.RegularExpressions.Match item in coll1)
		{
			Console.WriteLine(item.Groups[0]);
            Console.WriteLine(item.Groups[1]);
        }
        Console.WriteLine();
        Console.WriteLine(coll1.Count);
        break;
    case "e":
	case "exit":
		break;
	default:
		break;
}
```

> `Stack<char> stack = new Stack<char>();`**堆栈(后进先出)**
>
> `Push(T item)：`将元素添加到栈顶。
> `Pop()：`移除并返回栈顶元素。
> `Peek()：`返回栈顶元素，但不移除它。
> `Count `属性：获取栈中元素的个数。

```c#
public bool IsValid(string s)
    {
        Stack<char> stack=new Stack<char>();
        foreach (var c in s.ToCharArray())
        {
            if (c == '{')
            {
                stack.Push('}');
            }
            else if (c == '[')
            {
                stack.Push(']');
            }
            else if (c == '(')
            {
                stack.Push(')');
            }
            else if(stack.Count == 0 || stack.Pop()!=c)
            {
                return false;
            }
        }
        return (stack.Count == 0);
    }
//原题来自有效括号
```

### Lambda
> (x => x * x) 是一个 Lambda 表达式，其中 x 是输入参数，x * x 是表达式，表示对输入参数 x 进行平方运算。
> 接下来，我们将这个 Lambda 表达式赋值给一个 Func<int, int> 委托类型的变量 square，从而创建了一个委托实例。
> 最后，我们调用这个委托实例，传入参数 5，并将返回值赋给变量 result，从而得到了 5 的平方值 25。
```c#
Func<int, int> square = x => x * x;
int result = square(5); // result 的值为 25
```

