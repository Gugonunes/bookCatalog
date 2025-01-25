from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError

from users.models import Role


@login_required
def user_page(request):
    user = request.user

    if request.method == 'POST':
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        bio = request.POST.get('bio', '').strip()
        role_name = request.POST.get('role_name', '').strip()
        role_seniority = request.POST.get('role_seniority', '').strip()
        linkedin_url = request.POST.get('linkedin_url', '').strip()
        github_url = request.POST.get('github_url', '').strip()
        profile_picture = request.FILES.get('profile_picture')

        try:
            if full_name:
                first_name, *last_name = full_name.split(' ', 1)
                user.first_name = first_name
                user.last_name = ' '.join(last_name) if last_name else ''
            if email:
                user.email = email
            if bio:
                user.bio = bio
            if role_name and role_seniority:
                role, created = Role.objects.get_or_create(
                    name=role_name,
                    seniority=role_seniority
                )
                user.role = role
            if linkedin_url:
                user.linkedin_url = linkedin_url
            if github_url:
                user.github_url = github_url
            if profile_picture:
                user.profile_picture = profile_picture

            user.save()

            messages.success(request, 'Suas informações foram atualizadas com sucesso.')
            return redirect('user_page')

        except ValidationError as e:
            messages.error(request, f'Erro de validação: {e.message}')
        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao salvar suas informações.')

    return render(request, 'users/index.html', {'user': user})
