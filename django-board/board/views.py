from django.shortcuts import render, redirect, reverse
from .models import Board

def index(request):
    return render(request, 'board/index.html')

# 게시글 목록
def list(request):
    board_list = Board.objects.all().order_by('-id')
    context = {
        'board_list':board_list,
    }
    return render(
        request,
        'board/list.html',
        context
    )

# 게시글 조회
def read(request, id):
    board = Board.objects.get(pk=id)
    board.incrementReadCount()
    return render(request, 'board/read.html', {'board':board})

# 게시글 등록
def regist(request):
    if request.method == 'POST':
        title = request.POST['title']
        writer = request.POST.get('writer')
        content = request.POST['content']
        Board(title=title, writer=writer, content=content).save()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/regist.html')
    
# 게시글 수정
def edit(request, id):
    board = Board.objects.get(pk=id)
    if request.method == 'POST':
        board.title = request.POST['title']
        board.writer = request.POST.get('writer')
        board.content = request.POST['content']
        board.save()
        return redirect(reverse('board:read', args=(id,)))
    else:
        return render(request, 'board/edit.html', {'board':board})
    
# 게시글 삭제
def remove(request, id):
    board = Board.objects.get(pk=id)
    if request.method == 'POST':
        board.delete()
        return redirect(reverse('board:list'))
    else:
        return render(request, 'board/remove.html', {'board':board})