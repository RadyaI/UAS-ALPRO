import streamlit as st
import heapq
import graphviz

st.set_page_config(page_title="UAS Algoritma", layout="wide")

# --- CLASS DEFINITIONS ---
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# --- HUFFMAN FUNCTIONS ---
def build_huffman_tree(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0] if heap else None

def generate_huffman_codes(node, prefix="", code_map={}):
    if node:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", code_map)
        generate_huffman_codes(node.right, prefix + "1", code_map)
    return code_map

def draw_huffman(node, dot=None):
    if dot is None:
        dot = graphviz.Digraph()
        dot.attr('node', shape='circle', style='filled', color='lightblue')
    
    if node:
        label = f"{node.freq}\n({node.char})" if node.char else f"{node.freq}"
        dot.node(str(id(node)), label)
        if node.left:
            dot.edge(str(id(node)), str(id(node.left)), label="0")
            draw_huffman(node.left, dot)
        if node.right:
            dot.edge(str(id(node)), str(id(node.right)), label="1")
            draw_huffman(node.right, dot)
    return dot

# --- BINARY TRAVERSAL FUNCTIONS ---
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def get_traversal(root, method):
    res = []
    if root:
        if method == "PreOrder": res.append(root.val)
        res = res + get_traversal(root.left, method)
        if method == "InOrder": res.append(root.val)
        res = res + get_traversal(root.right, method)
        if method == "PostOrder": res.append(root.val)
    return res

def draw_bst(root, dot=None):
    if dot is None:
        dot = graphviz.Digraph()
        dot.attr('node', shape='circle', style='filled', color='lightgreen')
    
    if root:
        dot.node(str(root.val), str(root.val))
        if root.left:
            dot.edge(str(root.val), str(root.left.val))
            draw_bst(root.left, dot)
        if root.right:
            dot.edge(str(root.val), str(root.right.val))
            draw_bst(root.right, dot)
    return dot

# --- SETUP SESSION STATE ---
if 'active_page' not in st.session_state:
    st.session_state.active_page = "Huffman"

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigasi Project")
st.sidebar.write("Pilih Modul:")

if st.sidebar.button("🗜️ Huffman Coding", use_container_width=True):
    st.session_state.active_page = "Huffman"

if st.sidebar.button("🌳 Binary Tree", use_container_width=True):
    st.session_state.active_page = "BST"

st.sidebar.markdown("---")
st.sidebar.caption("UAS Algoritma Pemrograman")

# --- MAIN CONTENT ---
st.title("Project UAS: Algoritma Pemrograman - F")

st.info("""
    **Anggota Kelompok:**
    * Nur Aini (202410370110381)
    * Muhammad Radya Iftikhar (202410370110370)
    * Ayshea Marvella Pasha (202410370110379)
    * Alifia Nadia Ruksana (202410370110334)
    """)

if st.session_state.active_page == "Huffman":
    st.header("1. Huffman Coding Visualization")
    st.caption("Implementasi kompresi data menggunakan struktur pohon.")
    
    user_input = st.text_input("Masukkan teks untuk dikompresi:", "teks")
    
    if user_input:
        root = build_huffman_tree(user_input)
        codes = generate_huffman_codes(root, code_map={}) 
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Hasil Encode")
            encoded_str = ""
            for char in user_input:
                encoded_str += codes[char]
            
            st.code(encoded_str, language="text")
            st.metric("Bit Asli (8 bit/char)", len(user_input) * 8)
            st.metric("Bit Huffman", len(encoded_str))
            
            st.write("Tabel Kode:")
            st.table(codes)

        with col2:
            st.subheader("Visualisasi Pohon Huffman")
            if root:
                graph = draw_huffman(root)
                st.graphviz_chart(graph)

elif st.session_state.active_page == "BST":
    st.header("2. Binary Tree Traversal")
    st.caption("Visualisasi PreOrder, InOrder, dan PostOrder.")
    
    input_nums = st.text_input("Masukkan angka (pisahkan dengan koma):", "50, 30, 20, 40, 70, 60, 80")
    
    if input_nums:
        try:
            nums = [int(x.strip()) for x in input_nums.split(",")]
            root_bst = None
            for n in nums:
                root_bst = insert_bst(root_bst, n)
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.subheader("Kontrol")
                if st.button("Hitung Traversal"):
                    pre_res = get_traversal(root_bst, "PreOrder")
                    in_res = get_traversal(root_bst, "InOrder")
                    post_res = get_traversal(root_bst, "PostOrder")
                    
                    st.success(f"**PreOrder:** {pre_res}")
                    st.info(f"**InOrder:** {in_res}")
                    st.warning(f"**PostOrder:** {post_res}")
            
            with col2:
                st.subheader("Visualisasi Binary Search Tree")
                if root_bst:
                    graph = draw_bst(root_bst)
                    st.graphviz_chart(graph)
        except ValueError:
            st.error("Input harus berupa angka dipisah koma!")