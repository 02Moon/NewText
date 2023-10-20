### Print

Stream 流打印 Java 数组

1. 第一种

```java
Arrays.asList(arr).stream().forEach(s -> System.out.print(s))
```

2. 第二种

```java
Stream.of(arr).forEach(System.out.println);
```

3. 第三种

```
Arrays.stream(arr).forEach(System.out::println);
```

4. 第四种

```java
String[][] deepArray = new String[][] {{"沉默", "王二"}, {"一枚有趣的程序员"}};
System.out.println(Arrays.deepToString(deepArray));
```

​	打印结果

```tex
[[沉默, 王二], [一枚有趣的程序员]]
```
