# Form 表单容器

用于收集表单项数据、统一触发校验并提交结果。

---



 # API
 ## Props
无（表单配置通过子 Field 组件注册提供）

## Events
| 事件名    | 参数类型                                                     | 说明           |
| ------ | -------------------------------------------------------- | ------------ |
| submit | 无参数                         | 校验通过时触发，返回数据 |
| failed | `{ messages: Array<{ name: string, message: string }> }` | 校验失败时触发      |

## Slots

| 名称      | 说明                  |
| ------- | ------------------- |
| default | 用于放置表单项（Field）和提交按钮 |

# 搭配 Field 使用
必须满足以下条件，才会参与校验
1. 包含name和rules的yx-field组件
2. 使用传统form形式提交表单
3. 校验成功才会触发submit事件
``` vue
<template>
    <yx-form v-else @submit="handleSubmit">
        <yx-cell-group title="账户信息">
            <yx-field title="姓名" name="userName" v-model="form.userName" :rules="rules.userName"  />
        </yx-cell-group>
        <u-button type="primary" 
			shape="circle" 
			class="btn-area-submits"
			hover-class="none"
			form-type="submit"
			style="margin: 30rpx 0">提交</u-button>
    </yx-form>
</template>

<script setup>
    import { reactive,ref } from 'vue'

    const form = reactive({
        userName:null
	})

    const rules = reactive({
		userName:[{ required:true,message:"请输入用户名",trigger:['blur','changed'] }],
	})

    const handleSubmit = async function(){
        console.log("表单校验成功！")    
    }
</script>
```