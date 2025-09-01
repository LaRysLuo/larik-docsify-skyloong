# Field 表单项容器

`Field` 是与 `Form` 搭配使用的表单输入组件。支持必填、长度、正则与自定义函数校验；内置 `select` 选择模式（基于 `yx-picker`）

# 代码演示

## 基础用法
```vue
<template>
  <yx-form @submit="onSubmit">
    <yx-field
      name="username"
      title="用户名"
      v-model="form.username"
      :rules="[{ required: true, message: '请输入用户名', trigger: ['blur','submit'] }]"
    />
    <yx-field
      name="password"
      title="密码"
      type="password"
      v-model="form.password"
      :rules="[
        { required: true, message: '请输入密码', trigger: ['blur','submit'] },
        { min: 6, message: '至少 6 个字符', trigger: ['change','submit'] }
      ]"
    />
    <u-button form-type="submit">提交</button>
  </yx-form>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({
  username: '',
  password: ''
})

const onSubmit = (data) => {
  console.log('提交通过', data)
}
</script>
```

## 选择器用法
``` vue
<template>
<yx-field
  name="school"
  title="学校"
  type="select"
  v-model="form.schoolId"
  picker-title="选择学校"
  :columns="schoolOptions"
  :columns-fields="{ text: 'text', value: 'value' }"
  :rules="[{ required: true, message: '请选择学校', trigger: ['submit'] }]"
/>
</template>
<script setup>
const form = reactive({
  schoolId: null,
})
const schoolOptions = [
  { text: '一中', value: 1 },
  { text: '二中', value: 2 },
  { text: '三中', value: 3 },
]
</script>
```

# Api
## Props

| 参数              | 说明                                                 | 类型                                | 默认值                              |
| --------------- | -------------------------------------------------- | --------------------------------- | -------------------------------- |
| `modelValue`    | 绑定值（`select` 模式下为选项 `value`；普通输入为字符串值）             | `string \| number`                | `''`                             |
| `title`         | 左侧标题（由 `u-cell-item` 显示）                           | `string`                          | `-`                              |
| `name`          | 字段名（用于 `Form` 收集与校验）                               | `string`                          | `-`                              |
| `placeholder`   | 占位提示                                               | `string`                          | `'请输入'`                          |
| `type`          | 输入类型：`text`/`password`/`number`/`digit`/`select` 等 | `string`                          | `-`                              |
| `pickerTitle`   | 选择器标题（仅 `type='select'` 有效）                        | `string`                          | `-`                              |
| `columns`       | 选择器选项（仅 `type='select'` 有效）                        | `Array<{ text:any; value:any }>`  | `[]`                             |
| `columnsFields` | 选项字段映射 `{ text: 'text', value: 'value' }`          | `{ text: string; value: string }` | `{ text:'text', value:'value' }` |
| `maxlength`     | 最大长度                                               | `number`                          | `-`                              |
| `disabled`      | 禁用输入（`select` 模式下输入框始终禁用，仅能点开选择器）                  | `boolean`                         | `false`                          |
| `rules`         | 校验规则数组（见下文 **校验规则**）                               | `Array<Rule>`                     | `[]`                             |
## 校验规则
| 属性          | 类型                                                | 说明                                                             | 默认值          |
| ----------- | ------------------------------------------------- | -------------------------------------------------------------- | ------------ |
| `required`  | `boolean`                                         | 是否必填，若值为空则不通过                                                  | `false`      |
| `min`       | `number`                                          | 最小长度（仅字符串有效）                                                   | `-`          |
| `max`       | `number`                                          | 最大长度（仅字符串有效）                                                   | `-`          |
| `pattern`   | `RegExp`                                          | 正则表达式校验                                                        | `-`          |
| `validator` | `(value, ctx) => boolean \| string \| Promise`    | 自定义校验函数；返回 `true` 或 `''` 表示通过；返回 `false` 或字符串则校验失败（字符串会作为错误提示） | `-`          |
| `message`   | `string`                                          | 错误提示文本                                                         | `-`          |
| `trigger`   | `'blur' \| 'change' \| 'submit' \| Array<string>` | 校验触发时机，`submit` 总是会执行                                          | `['submit']` |

## Events
| 事件名                 | 说明                          |
| ------------------- | --------------------------- |
| `update:modelValue` | 当输入值变化时触发，用于 `v-model` 双向绑定 |
| `change`            | 输入值变化时触发                    |
| `focus`             | 输入框获得焦点时触发                  |
| `blur`              | 输入框失去焦点时触发                  |

# 与 Form 集成
每个 Field 会自动向 Form 注册：

validate(trigger)：按规则执行校验；

getValue()：返回当前值。

Form 在提交时会逐一调用 validate，若有失败则触发 failed，全部通过触发 submit。

