    sumaR = 0
    sumaG = 0
    sumaB = 0
    r2 = 0
    g2 = 0
    b2 = 0
    
    KB = 0
    KG = 0
    KR = 0
    #nombre_img= entrada.get()
    img = askopenfilename()
    esta_hueva = cv2.imread(img)
    
    imagen = Gamma(esta_hueva)
    #nombre_img = desdistorcion(nombre_img2)
    valorMaxB = np.amax(imagen[:, :, 0])
    valorMaxG = np.amax(imagen[:, :, 1])
    valorMaxR = np.amax(imagen[:, :, 2])
    
    imagen[:, :, 0] = (imagen[:, :, 0]/valorMaxB) * 255
    imagen[:, :, 1] = (imagen[:, :, 1]/valorMaxG) * 255
    imagen[:, :, 2] = (imagen[:, :, 2]/valorMaxR) * 255
    cv2.imwrite("original.jpg", imagen)
    #nombre_img = desdistorcion(nombre_img2)  # imagen desdistorcionada
    #cv2.imshow("hola",nombre_img)
    cv_img = imagen

    cv_img2 = cv_img.copy()

    fil = cv_img.shape[0] #y
    col = cv_img.shape[1] #x

    for x in range(col):
        for y in range(fil):
            
            r2 = r2 + cv_img.item(y,x,2)
            g2 = g2 + cv_img.item(y,x,1)
            b2 = b2 + cv_img.item(y,x,0)

    print("r2:"+str(r2)) 
    print("g2:"+str(g2)) 
    print("b2:"+str(b2)) 
    
    KB = 1
    KG = r2/b2
    KR = r2/r2

    print("Kb:"+str(KB))
    print("Kg:"+str(KG))
    for x in range(col):
        for y in range(fil):
            RED = cv_img.item(y,x,2) * KR
            GREEN = cv_img.item(y,x,1) * KG

            cv_img2.itemset((y,x,0), cv_img.item(y,x,0))
            cv_img2.itemset((y,x,1), GREEN)
            cv_img2.itemset((y,x,2), RED)
    cv2.imwrite("codificado.jpg",cv_img2)
    cv2.imshow("original - Gray-world", cv2.imread("original.jpg"))
    cv2.imshow("Gray-world", cv2.imread("codificado.jpg"))
    cv2.waitKey(0)
    cv2.destroyAllWindows()