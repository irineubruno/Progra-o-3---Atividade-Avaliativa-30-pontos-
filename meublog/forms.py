from django import forms
from django.core.mail import EmailMessage

from meublog.models import Comentario


class EmailForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    destino = forms.EmailField()
    coments = forms.CharField(required=False, widget=forms.Textarea)

    def enviar_email(self, meupost):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        destino = self.cleaned_data['destino']
        coments = self.cleaned_data['coments']

        conteudo = f'Leia o post: {meupost.titulo}\n'\
                   f'Comentários: {coments}'

        mail = EmailMessage(
            subject=f'{nome} recomenda ler o Post{meupost.titulo}',
            body=conteudo,
            from_email=email,
            to=[destino],
            headers={'Reply-To': email}
        )
        mail.send()


class ComentarPostForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome', 'email', 'corpo']

    def salvar(self, post):
        comentario = self.save(commit=False)
        comentario.post = post
        comentario.nome = self.cleaned_data['nome']
        comentario.email = self.cleaned_data['email']
        comentario.corpo = self.cleaned_data['corpo']
        return comentario.save()
