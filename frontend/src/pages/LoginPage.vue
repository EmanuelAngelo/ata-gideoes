<template>
  <section class="min-h-screen bg-slate-950 text-slate-50">
    <div class="mx-auto flex min-h-screen max-w-7xl flex-col lg:flex-row">
      <div class="flex flex-1 items-center justify-center px-6 py-12 sm:px-10 lg:px-16">
        <LoginForm
          :loading="isSubmitting"
          :error-message="errorMessage"
          :initial-username="lastUsername"
          @submit="handleSubmit"
        />
      </div>

      <aside class="relative hidden flex-1 overflow-hidden lg:flex">
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_top,_rgba(99,102,241,0.35),_transparent_35%),linear-gradient(160deg,_rgba(15,23,42,1)_10%,_rgba(30,41,59,1)_45%,_rgba(49,46,129,0.95)_100%)]" />
        <div class="relative flex w-full flex-col justify-between px-12 py-16">
          <div>
            <p class="text-sm font-semibold uppercase tracking-[0.3em] text-indigo-300">Secretaria digital</p>
            <h2 class="mt-6 max-w-md text-4xl font-bold leading-tight text-white">
              Organize atas de reuniões com um fluxo moderno e confiável.
            </h2>
            <p class="mt-6 max-w-xl text-base leading-7 text-slate-300">
              Esta é a base do novo frontend da ATA: autenticação integrada ao backend Django,
              separação clara entre API, estado e interface, e evolução preparada para módulos futuros.
            </p>
          </div>

          <div class="grid gap-4">
            <div class="rounded-3xl border border-white/10 bg-white/5 p-5 backdrop-blur">
              <p class="text-sm font-semibold text-white">Padrão de arquitetura</p>
              <p class="mt-2 text-sm leading-6 text-slate-300">
                Camada `api`, store de autenticação isolada e componente de formulário desacoplado.
              </p>
            </div>
            <div class="rounded-3xl border border-white/10 bg-white/5 p-5 backdrop-blur">
              <p class="text-sm font-semibold text-white">Experiência consistente</p>
              <p class="mt-2 text-sm leading-6 text-slate-300">
                Login 100% Tailwind, sem depender da renderização visual do Vuetify para manter o layout limpo.
              </p>
            </div>
          </div>
        </div>
      </aside>
    </div>
  </section>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { ApiError } from '@/api'
  import LoginForm from '@/components/LoginForm.vue'
  import { useAuthStore } from '@/stores/auth'

  const router = useRouter()
  const authStore = useAuthStore()

  const isSubmitting = ref(false)
  const errorMessage = ref('')
  const lastUsername = ref(authStore.username)

  async function handleSubmit(payload: {
    username: string
    password: string
    rememberMe: boolean
  }) {
    errorMessage.value = ''
    lastUsername.value = payload.username

    if (!payload.username.trim() || !payload.password.trim()) {
      errorMessage.value = 'Preencha usuário e senha para continuar.'
      return
    }

    isSubmitting.value = true

    try {
      await authStore.login({
        username: payload.username.trim(),
        password: payload.password,
      })

      router.push({ name: 'dashboard' })
    } catch (error) {
      if (error instanceof ApiError) {
        errorMessage.value = error.message || 'Não foi possível autenticar com o backend.'
      } else {
        errorMessage.value = 'Erro inesperado ao tentar entrar. Tente novamente.'
      }
    } finally {
      isSubmitting.value = false
    }
  }
</script>
