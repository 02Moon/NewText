`List<List<double>> = inputDate`

list第一层长度

```c#
int n = inputData.ToArray().Length;
```

list第二层长度

```c#
int n = inputData.ToArray().Length;
```

`double` 转`int`不进行四舍五入

```c#
(int)(2.5d)
Math.Round(4.5,MidpointRounding.ToEven)
4
```

`double` 转`int`进行四舍五入

```c#
Convert.ToInt32(2.5d)
Math.Round(4.5,MidpointRounding.AwayFromZero)
5
```

数据中删除重复值并排序

```c#
string str = "11223344"
var s = str.Distinct().OrderBy(x=>x).Reverse().ToArray();
```

`String`转型`Long`

```c#
result = long.Parse(st);
```

`Linq`筛选条件查找

```c#
List = List.Where(x=>.getName() <= Num).ToList();
```

`EXIT`

```c#
Environment.Exit(0);
```

`doubel`保留一位小数

`MidpointRounding.AwayFromZero`——参数设置四舍五入，误判断基偶数

```c#
Math.Round((double)sum / numberOfPassedGoodList.Count, 1,MidpointRounding.AwayFromZero);
Math.Round(*double*,1)
double a = (double)sum / (double)numberOfPassedGoodList.Count;
string str = a.ToString("f1");
averageScore = double.Parse(str);
```

字符串中的`空格`换成`%20`

```c#
String s = "we are human";
Cosole.write(string.Join("" , s.Select(c =>c==' ' ? "%20" : c + "")));
```

`正则表达式`的应用

```c#
Regex reg = new Regex("[0-9]");
if(reg.IsMatch(xxx)){
}
```

在数组中找出重复项并只保留一个其他的删除

> `HashSet`只能存储单个元素，而`Hashtable`可以存储键值对。

```c#
string[] arr = { "AS", "QWER", "ZXV", "HJKL", "YO", "QWER", "VBNM", "FGH", "QWER", "ABCD", "YO", "QWER", "FGH", "YO" };
HashSet<string> set = new HashSet<string>(arr);
string[] result = new string[set.Count];
set.CopyTo(result);
```

数组的`intersect`方法

```c#
 List<string> list1 = new List<string>() { "A", "B", "C" };
List<string> list2 = new List<string>() { "B", "C", "D" };
ArrayList ll = new ArrayList(list1.Intersect(list2).ToArray());
//ll中数据为"B","C"
```

数组的数据相加

```c#
int[] iii = { 3,2,2,3 };
iii.Aggregate((x, y) => (x + y));
```

数据之间加符号

```c#
int[] iii = { 3,2,2,3 };
string.Join("#",iii)
//"3#2#2#3"
```

Groupby去重

```c#
var uniqueData = dataSource.GroupBy(item => item).Select(group => group.First()).ToList();
```

​	它使用 Where() 方法来筛选出数组中的偶数，其中第一个参数是一个 lambda 表达式，用于判断数组元素是否为偶数，第二个参数是一个 lambda 表达式，用于指定筛选出的元素的类型。在这个例子中，第二个参数是 x => x，表示筛选出的元素类型为 int。

```c#
using StructLinq;
int[] array = new [] {1, 2, 3, 4, 5};
int result = array .ToStructEnumerable() .Where(x => (x & 1) == 0, x=>x) .Select(x => x *2, x => x) .Sum();
```

在item的显示中为 item{Number = 2 , Square = 4}

```c#
int[] numbers = { 1, 2, 3, 4, 5 };

var query = from n in numbers
            let square = n * n
            where square > 10
            select new { Number = n, Square = square };

foreach (var item in query)
{
    Console.WriteLine("Number = {0}, Square = {1}", item.Number, item.Square);
}
```

Test

```c#
var products = new List<string>() {"Basketball", "Baseball", "Tennis Raquet", "Running Shoes", "Wrestling Shoes", "Soccer Ball", "Football", "Shoulder Pads",
                "Trail Running Shoes", "Cycling Shoes", "Kayak", "Kayak Paddles"};
            //声明一个变量kayakProducts并将其设置为等于所有包含单词“Kayak”的产品

            var kayakProducts = products.Where(x => x.Contains("Kayak") == true);

            //使用 foreach 循环将 kayakProducts 打印到控制台。

            foreach (var item in kayakProducts)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            //声明一个变量shoeProducts并将其设置为等于所有包含单词“Shoes”的产品

            var shoeProducts = products.Where(x => x.Contains("Shoes"));

            //使用foreach循环将shoeProducts打印到控制台。

            foreach(var item in shoeProducts)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            //声明一个变量 ballProducts 并将其设置为等于名称中包含 ball 的所有产品。

            var ballProducts = products.Where(x => x.Contains("ball"));

            //使用 foreach 循环将 ballProducts 打印到控制台。

            foreach (var item in ballProducts)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            //按字母顺序对 ballProducts 进行排序并将其打印到控制台。

            ballProducts = ballProducts.OrderBy(x => x.First());

            //使用.First()扩展将具有最长名称的产品打印到控制台。

            Console.WriteLine(products.ToList().OrderByDescending(x=>x.Length).First());
            Console.WriteLine();

            //使用.First()扩展名将名称最短的产品打印到控制台。

            Console.WriteLine(products.ToList().OrderBy(x=>x.Length).First());
            Console.WriteLine();

            //使用索引将名称第四短的产品打印到控制台（必须使用.ToList()将结果转换为列表）。

		   //var fourthshortestName = products.OrderBy(x => x.Length).ToList()[3];
            Console.WriteLine(products.OrderBy(x=>x.Length)
            .ThenBy(x=>x)//如长度一样按照字典序排序
            .Skip(3)//跳过前三个数据
            .FirstOrDefault());
            Console.WriteLine();

            //使用索引将名称第二长的 ballProduct 打印到控制台（必须使用 .ToList() 将结果转换为列表）。

            Console.WriteLine(ballProducts.OrderByDescending(x=>x.Length).ThenBy(x=>x).Skip(1).FirstOrDefault());
            Console.WriteLine();

            //声明一个变量reverseProducts并将其设置为等于按最长单词优先排序的所有产品。 （使用 OrderByDecending() 扩展）。

            var reverseProducts = products.OrderByDescending(x => x.Length);

            //使用foreach循环将reverseProducts打印到控制台。

            foreach (var item in reverseProducts)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();
```

