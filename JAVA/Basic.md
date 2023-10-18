> JVM	`Java Virtual Machine(Java 虚拟机)`
> 
> JDK	`Java Development Kit(Java 开发工具包)`
> 
> JRE	`Java Runtime Environment(Java 运行环境)`

### 访问修饰符

> - Default	`默认，什么都不写`
> - Private	`在同一类内可见`
> - Public	`对所有类可见`
> - Protected	`对同一包内的类和所有子类可见`
>
> |   可见性   | private | Default | Protected | Public |
> | :--------: | :-----: | :-----: | :-------: | :----: |
> | 同一个类中 |    √    |    √    |     √     |   √    |
> | 同一个包中 |    X    |    √    |     √     |   √    |
> |   子类中   |    X    |    X    |     √     |   √    |
> |  全局范围  |    X    |    X    |     X     |   √    |
>

### Integer

> 如果整型字面是值在-128 到 127 之间，那么自动装箱是不会 new 新的 Integer 对象，而是直接引用缓存池中的 Integer 对象

```java
  public static void main(String[] args) {
        Integer a = 127;
        Integer b = 127;
        Integer b1 = new Integer(127);
        System.out.println(a == b); //true
        System.out.println(b==b1);  //false

        Integer c = 128;
        Integer d = 128;
        System.out.println(c == d);  //false
    }
```

> `Integer.ValueOf()`
> 判断是否存在缓存区，如存在直接返回缓存池的对象，而不是创建一个新的对象，这样可以节省内存空间。

```java
Integer a = Integer.valueOf(100);
Integer b = Integer.valueOf(100);
```

### String 转成 Integer (原理)

>String 转成 Integer，主要有两种方法
> - Integer.parseInt(String s)
> - Integer.valueOf(String s)
>
>不管哪种都会调用 Integer 类中的 `parseInt(String s, int radix)`方法

```java
public static int parseInt(String s, int radix)
                throws NumberFormatException
    {
        int result = 0;
        //是否是负数
        boolean negative = false;
        //char字符数组下标和长度
        int i = 0, len = s.length();
        ……
        int digit;
        //判断字符长度是否大于0，否则抛出异常
        if (len > 0) {
            ……
            while (i < len) {
                // Accumulating negatively avoids surprises near MAX_VALUE
                //返回指定基数中字符表示的数值。（此处是十进制数值）
                digit = Character.digit(s.charAt(i++),radix);
                //进制位乘以数值
                result *= radix;
                result -= digit;
            }
        }
        //根据上面得到的是否负数，返回相应的值
        return negative ? result : -result;
    }
```

### Try Catch

> try 返回前先执行 finally，结果 finally 里不按套路出牌，直接 return 了，自然也就走不到 try 里面的 return 了。
> `执行结果：3`

```java
public class TryDemo {
    public static void main(String[] args) {
        System.out.println(test1());
    }
    public static int test1() {
        try {
            return 2;
        } finally {
            return 3;
        }
    }
}
```

### Stream流

```java
List<String> stringCollection = new ArrayList<>();
stringCollection.add("ddd2");
stringCollection.add("aaa2");
stringCollection.add("bbb1");
stringCollection.add("aaa1");
stringCollection.add("bbb3");
stringCollection.add("ccc");
stringCollection.add("bbb2");
stringCollection.add("ddd1");
```

中间操作

- `filter(Predicate<T> predicate)`：过滤符合条件的元素。

```java
stringCollection
    .stream()
    .filter((s) -> s.startsWith("a"))
    .forEach(System.out::println);

// "aaa2", "aaa1"
```

- `map(Function<T, R> mapper)`：将元素进行映射转换。

```java
stringCollection
    .stream()
    .map(String::toUpperCase)
    .sorted((a, b) -> b.compareTo(a))
    .forEach(System.out::println);

// "DDD2", "DDD1", "CCC", "BBB3", "BBB2", "AAA2", "AAA1"
```

- `sorted(Comparator<T> comparator)`：对元素进行排序。
- `distinct()`：去除重复元素。
- `limit(long maxSize)`：限制元素数量。

终端操作

- forEach(Consumer<T> action)：对每个元素执行指定操作。
- toArray()：将Stream流转换为数组。
 - reduce(T identity, BinaryOperator<T> accumulator)：对元素进行累加操作。

```java
Optional<String> reduced =
    stringCollection
        .stream()
        .sorted()
        .reduce((s1, s2) -> s1 + "#" + s2);

reduced.ifPresent(System.out::println);
// "aaa1#aaa2#bbb1#bbb2#bbb3#ccc#ddd1#ddd2"
```

 - collect(Collector<T, A, R> collector)：将元素收集到集合中。
 - count()：统计元素数量。
- anyMatch(Predicate<T> predicate)：判断是否存在符合条件的元素。
 - allMatch(Predicate<T> predicate)：判断是否所有元素都符合条件。
 - noneMatch(Predicate<T> predicate)：判断是否不存在符合条件的元素。
 - findFirst()：返回第一个元素。
 - findAny()：返回任意一个元素
 - sorted(Comparator<T> comparator)：对元素进行排序。

```java
stringCollection
    .stream()
    .sorted()
    .filter((s) -> s.startsWith("a"))
    .forEach(System.out::println);

// "aaa1", "aaa2"
```
