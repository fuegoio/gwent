<template>
    <v-img id="card" :src="image"></v-img>
</template>

<script>
    export default {
        name: "Card",
        props: {
            image: {type: String, required: true}
        }
    }
</script>

<style scoped>
    #card {
        max-height: 300px;
        max-width: 150px;
        border-radius: 18px;
    }

    .full-height {
        height: 100%;
    }
</style>