### **步骤 1：以管理员身份打开命令提示符**

1. 按 `Win + X` 并选择 **命令提示符（管理员）** 或 **Windows 终端（管理员）**。
2. 如果你不是管理员，你就完蛋了。先获得管理员访问权限。

---

### **步骤 2：列出所有事件日志**

在深入研究安全日志之前，让我们先看看有哪些日志可用：

```cmd
wevtutil el
```

这将列出所有事件日志。在列表中查找“Security”——这就是您想要的。

---

### **步骤 3：查询安全日志**

要查看安全日志，请使用以下命令：

```cmd
wevtutil qe Security /f:text
```

- `qe`：查询事件。
- `Security`：日志名称。
- `/f:text`：以纯文本格式输出（更易于阅读）。

这会将整个安全日志转储到命令提示符。

---

### **步骤 4：过滤特定事件**

安全日志可能非常庞大，因此您可能需要过滤特定事件。使用 `/q` 标志应用 XPath 查询。

#### **示例 1：查找失败的登录**

要查找失败的登录尝试（事件 ID 4625）：

```cmd
wevtutil qe Security /q:"*[System[(EventID=4625)]]" /f:text
```

#### **示例 2：查找成功的登录**

要查找成功的登录（事件 ID 4624）：

```cmd
wevtutil qe Security /q:"*[System[(EventID=4624)]]" /f:text
```

#### **示例 3：查找帐户锁定**

要查找帐户锁定（事件 ID 4740）：

```cmd
wevtutil qe Security /q:"*[System[(EventID=4740)]]" /f:text
```

---

### **步骤5：导出安全日志**

如果您想要将安全日志保存到文件中以供日后分析，请使用以下命令：

```cmd
wevtutil qe Security /f:text > C:\SecurityLog.txt
```

这会将日志保存到 `C:\SecurityLog.txt`。

---

### **步骤 6：清除安全日志（可选）**

如果您已完成侦查并想要掩盖您的踪迹，请清除安全日志：

```cmd
wevtutil cl Security
```

这会将日志清除干净。

---

### **步骤 7：禁用安全日志记录（可选）**

如果您想要（暂时）停止记录新事件，请禁用安全日志：

```cmd
wevtutil sl Security /e:false
```

要稍后重新启用它：

```cmd
wevtutil sl Security /e:true
```
